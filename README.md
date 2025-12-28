# Web crawler "chorus" outage

Record Internet outage data in New Zealand

![](https://shields.io/badge/dependencies-Python_3.12-blue)

## Install

Create a Python virtual environment and activate.

Run the following command.

```
pip install -r requirements.txt
```

Create a PostgreSQL 17 database in [Neon](https://neon.com/) database, or your own PostgreSQL database.

Run `database_schema.sql` in database console to mock the database schema.

Include the following variables into environment variables.

| Variable | Description                                                  |
| -------- | ------------------------------------------------------------ |
| NEON_DB  | Connection string to Neon database. If using other database, set to connection string of your own PostgreSQL database. |

## Usage

This program records the historical Internet outage from [chorus](https://www.chorus.co.nz/help/tools/internet-outages-map) website. "chorus" is the biggest Internet fiber provider which serves the majority of ADSL, VDSL, fiber Internet connection in New Zealand.

GitHub Actions record updated prices of the past day in 10:00 UTC every day.
