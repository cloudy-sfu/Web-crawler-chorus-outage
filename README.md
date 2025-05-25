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

It publishes a dataset at [Hugging Face](https://huggingface.co/datasets/cloudy-sfu/Chorus-outage/tree/main).

GitHub Actions record updated prices of the past day in 10:00 UTC every day.

- 22:00 New Zealand standard time
- 23:00 New Zealand daylight saving time
