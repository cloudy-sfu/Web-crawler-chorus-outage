# Web crawler "chorus" outage

Record Internet outage data in New Zealand

![](https://shields.io/badge/dependencies-Python_3.12-blue)

## Acknowledgement

Data source: [chorus](https://www.chorus.co.nz/help/tools/internet-outages-map)



## Install

Create a Python virtual environment and activate.

Run the following command.

```
pip install -r requirements.txt
```



## Usage

This program records the historical Internet outage from "chorus" website. "chorus" is the biggest Internet fiber provider which serves the majority of ADSL, VDSL, fiber Internet connection in New Zealand.

Go to "data" branch and download the data of any date. For example, folder `2025-04` means the data of 2025 April. File `2025-04-20` means the current Internet outage status at approximately (script triggered time may have about 10 minutes delay) 2025-04-20 10:00 UTC.

To parse the data, start with the following script.

```python
import pandas as pd

outage = pd.read_pickle("2025-04/2025-04-20")
```

The meaning of columns are as follows.

| Name                  | Data type                                                    | Description                                                  |
| --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `start_time`          | [`pandas.Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html) | The start time of outage.                                    |
| `incident_point`      | [`shapely.Point`](https://shapely.readthedocs.io/en/stable/reference/shapely.Point.html#shapely.Point) | The place of the label, which describes the incident, in chorus outage map. |
| `incident_area`       | [`shapely.MultiPolygon`](https://shapely.readthedocs.io/en/stable/reference/shapely.Point.html#shapely.Point) | The area that cannot access to Internet.                     |
| `role`                | `str`                                                        | Unknown.                                                     |
| `n_impacted_services` | `int`                                                        | The number of Internet services that are impacted.           |
| `description`         | `str`                                                        | Description.                                                 |
| `update_time`         | `pandas.Timestamp`                                           | The publishing time of latest update about this incident.    |
| `update_text`         | `str`                                                        | The content of latest update about this incident.            |

*Because the table contain shapely objects, no text format is provided.*

GitHub Actions record updated prices of the past day in 10:00 UTC every day.

- 22:00 New Zealand standard time
- 23:00 New Zealand daylight saving time

The data will be updated to "data" branch.

