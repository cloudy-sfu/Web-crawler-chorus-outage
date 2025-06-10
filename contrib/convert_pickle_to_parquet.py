from argparse import ArgumentParser
import os

import pandas as pd

parser = ArgumentParser()
parser.add_argument("--base_dir", type=str, required=True)
cmd, _ = parser.parse_known_args()
base_dir = cmd.base_dir


def shape_to_geo_json(x):
    if pd.isna(x):
        return pd.NA
    else:
        return x.__geo_interface__


for month_folder_name in os.listdir(base_dir):
    if month_folder_name.startswith("."):
        continue
    month_folder_path = os.path.join(base_dir, month_folder_name)
    if os.path.isdir(month_folder_path):
        for file_name in os.listdir(month_folder_path):
            if file_name.endswith(".parquet"):
                continue
            fp = os.path.join(month_folder_path, file_name)
            if os.path.isfile(fp):
                output_path = f"{fp}.parquet"
                outages = pd.read_pickle(fp)
                outages['incident_point'] = outages['incident_point'].apply(shape_to_geo_json)
                outages['incident_area'] = outages['incident_area'].apply(shape_to_geo_json)
                outages.to_parquet(output_path, engine='pyarrow')
                os.remove(fp)
