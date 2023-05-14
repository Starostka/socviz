import polars as pl
import matplotlib.pyplot as plt
import matplotx
import seaborn as sns
from datetime import date, time
from polars.dataframe import DataFrame
from rich import print
from pathlib import Path
from typing import Protocol
from dataclasses import dataclass
from scipy import stats

plt.style.use(matplotx.styles.dufte)

jobs = pl.read_csv('data/jobs_forecast.csv', ignore_errors=True, try_parse_dates=True)
jobs.columns
jobs.shape
jobs.describe()

jobs['Category'].unique()
list(jobs['Industry Space Use'].unique())

jobs_industry = jobs.filter(pl.col('Category') == 'Jobs by industry')

q = (jobs_industry
     .filter(pl.col('Industry Space Use') == 'Total jobs')
     .sort('Year')
     .groupby(['Geography', 'Year'], maintain_order=True)
     .agg(pl.sum('Value'))
     .with_columns([
         pl.col('Value').log().alias('Value_log'),
         pl.col('Year').cast(pl.UInt32)
     ]))
set(q['Geography'].unique())
q = q.filter(pl.col('Geography').is_in(['Melbourne (CBD)', 'Carlton', 'Kensington', 'Parkville', 'South Yarra', 'Southbank']))

plt.title("Job forecasts for areas")
sns.relplot(q, x='Year', y='Value', hue="Geography", kind="line")
plt.ylabel('Jobs')
plt.xlabel('Year')
plt.show()
