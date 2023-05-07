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

# Note: Working with forecast data requires us to take extra care in the
# accuracy/validity of the data. Thus, we should compare with historic data
# to confirm our points.

# 585 KB, 9114 rows, 5 cols, geodata: area name
jobs = pl.read_csv('data/jobs_forecast.csv', ignore_errors=True, try_parse_dates=True)
jobs.columns
jobs.shape
jobs.describe()

jobs['Category'].unique()
list(jobs['Industry Space Use'].unique())

jobs_industry = jobs.filter(pl.col('Category') == 'Jobs by industry')
jobs_space = jobs.filter(pl.col('Category') == 'Jobs by space use')

def unique_forecasts(data: DataFrame):
    """Unique forecast types"""
    return data['Industry Space Use'].unique()

def geo_forecast(data: DataFrame, forecast_type: str):
    """Return year and values for the specified forecast type"""
    return (data
         .filter(pl.col('Industry Space Use') == forecast_type)
         .sort('Year')
         .groupby('Geography').agg([pl.col('Year'), pl.col('Value')]))

# == Investigating jobs by industries
list(unique_forecasts(jobs_industry))

# Geographical forecasts for various types
geo_forecast(jobs_industry, 'Total jobs')
geo_forecast(jobs_industry, 'Accommodation')
geo_forecast(jobs_industry, 'Education and training')


# == Investigating jobs by space use
list(unique_forecasts(jobs_space))

# Geographical forecasts for various types
geo_forecast(jobs_space, 'Total jobs')
geo_forecast(jobs_space, 'Accommodation - Commercial')
geo_forecast(jobs_space, 'Education')