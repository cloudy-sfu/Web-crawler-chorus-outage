import re
import json
import logging
import sys

import pandas as pd
from requests import Session
from shapely.geometry import shape
from argparse import ArgumentParser

logging.basicConfig(
    handlers=[logging.StreamHandler(sys.stdout)],
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S',
)
session = Session()
parser = ArgumentParser()
parser.add_argument('--github_action', action='store_true')
cmd, _ = parser.parse_known_args()

# %% Load header.
with open("header/chorus_config.json") as f:
    header_config = json.load(f)
with open("header/chorus_incidents.json") as f:
    header_incidents = json.load(f)

# %% Get auth.
response = session.get(
    "https://www.chorus.co.nz/config.json", headers=header_config, timeout=3)
if response.status_code != 200:
    raise Exception(f"Status code: {response.status_code}. Reason: {response.reason}")
response_json = response.json()
auth = response_json['OUTAGES']['AUTH']
logging.info("Received the authentication key.")

# %% Get outage.
header_incidents['authorization'] = auth
response = session.get(
    "https://api.chorus.co.nz/events/v3/incidents",
    params=json.dumps({"includePolygons": "true"}),
    headers=header_incidents,
    timeout=3,
)
if response.status_code != 200:
    logging.error(f"Status code: {response.status_code}. Reason: {response.reason}")
incidents = response.json()
logging.info("Received the outages' data structure.")

# %% Parse outage map.
assert isinstance(incidents, list), "Fail to parse outages' data structure."
update_re = re.compile(r'(?P<update_time>\d{2}/\d{2}/\d{4} \d{2}:\d{2})')


def extract_update_time(text: str):
    """
    Extracts the update time from a log line of the form
    "dd/mm/YYYY hh:MM Update ...".
    Returns the timestamp string if matched, otherwise pd.NA.
    """
    match = update_re.search(text)
    if match:
        update_time_str = match.group('update_time')
        update_time_naive = pd.to_datetime(
            update_time_str, format="%d/%m/%Y %H:%M", errors="coerce")
        update_time = update_time_naive.tz_localize(
            tz='Pacific/Auckland', ambiguous='NaT', nonexistent='NaT')
        return update_time
    else:
        return pd.NaT


outages = []
for incident in incidents:
    sites = incident.get('sites', [])
    start_time_raw = incident.get('start_time')
    if start_time_raw is None:
        start_time = pd.NaT
    else:
        start_time_naive = pd.to_datetime(start_time_raw, unit='s')
        start_time_utc = start_time_naive.tz_localize(tz='UTC', nonexistent='NaT')
        start_time = start_time_utc.tz_convert('Pacific/Auckland')
    update_lines = incident.get('add_desc', '').split('\n')
    match len(update_lines):
        case 0:
            update_time_ = pd.NA
            update_text = pd.NA
        case 1:
            update_time_ = pd.NaT
            update_text = update_lines[0]
        case _:  # n_lines >= 2
            update_time_ = extract_update_time(update_lines[0])
            update_text = update_lines[1]
    description = incident.get('description', '')
    for site in sites:
        try:
            point = json.loads(site.get('point', ''))
            try:
                point = shape(point)
            except Exception as e:
                logging.error(f"Point of a site cannot be parsed. {e}")
                point = pd.NA
        except json.JSONDecodeError:
            point = pd.NA
        try:
            multi_polygon = json.loads(site.get('poly', ''))
            try:
                multi_polygon = shape(multi_polygon)
            except Exception as e:
                logging.error(f"Multi-polygon of a site cannot be parsed. {e}")
                multi_polygon = pd.NA
        except json.JSONDecodeError:
            multi_polygon = pd.NA
        site_ = {
            "start_time": start_time,
            "incident_point": point,
            "incident_area": multi_polygon,
            "role": site.get('role', pd.NA),
            "n_impacted_services": site.get('impact', pd.NA),
            "description": description,
            "update_time": update_time_,
            "update_text": update_text,
        }
        outages.append(site_)
outages = pd.DataFrame(outages)
record_date = pd.Timestamp.now(tz='UTC')
if cmd.github_action:
    outages.to_pickle(f"/tmp/{record_date.strftime("%Y-%m-%d")}")
else:
    outages.to_pickle(f"{record_date.strftime("%Y-%m-%d")}")
