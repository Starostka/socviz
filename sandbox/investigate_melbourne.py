import polars as pl
import matplotlib.pyplot as plt
import matplotx
from datetime import date, time
from polars.dataframe import DataFrame
from rich import print
from pathlib import Path
from typing import Protocol
from dataclasses import dataclass

plt.style.use(matplotx.styles.dracula)

# [X] What is the total size of your data? (MB, number of rows, number of variables, etc)
# [] What are other properties? (What is the date range? Is is it geo-data?, then a quick plot of locations, etc.)
# [] Show the fundamental distributions of the data (similar to the work we did on SF crime data for lecture 3)

# 585 KB, 9114 rows, 5 cols, geodata: area name
jobs_forecast = pl.read_csv('data/jobs_forecast.csv', ignore_errors=True, try_parse_dates=True)
jobs_forecast.columns
jobs_forecast.shape
jobs_forecast.describe()

# 710 KB, 17052 rows, 5 cols, geodata: area name
population_forecast = pl.read_csv('data/population_forecast.csv', ignore_errors=True, try_parse_dates=True)
population_forecast.columns
population_forecast.shape
population_forecast.describe()

# 161 KB, 2646 rows, 5 cols, geodata: area name
dwellings_and_household = pl.read_csv('data/dwellings_and_household.csv', ignore_errors=True, try_parse_dates=True)
dwellings_and_household.columns
dwellings_and_household.shape
dwellings_and_household.describe()

# 834 KB, 9996 rows, 5 cols, geodata: area name
floor_space = pl.read_csv('data/floor_space.csv', ignore_errors=True, try_parse_dates=True)
floor_space.columns
floor_space.shape
floor_space.describe()

plt.hist(x=floor_space['Category'])
plt.show()

# 328 KB, 1430 rows, 42 cols, geodata: yes
activity_monitor = pl.read_csv('data/activity_monitor.csv', ignore_errors=True, try_parse_dates=True)
activity_monitor.columns
activity_monitor.schema
activity_monitor.shape
activity_monitor.describe()

activity_monitor['street_address'].unique()

plt.hist(activity)

plt.hist(x=activity_monitor['student_apartments'])
plt.show()


# development activity completed, year, count, streets
q = ( activity_monitor.filter(pl.col('year_completed') != None) )
locations = q.groupby('year_completed').agg(pl.count(), pl.col('street_address'))
plt.bar(x = locations['year_completed'], height = locations['count'])
plt.title('Completed activities, temporal')
plt.ylabel('Count')
plt.xlabel('Years')
plt.show()