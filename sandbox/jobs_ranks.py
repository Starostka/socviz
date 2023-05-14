import polars as pl
import matplotlib.pyplot as plt
import matplotx
from datetime import date, time
from polars.dataframe import DataFrame
from rich import print
from pathlib import Path
from typing import Protocol
from dataclasses import dataclass
from scipy import stats

plt.style.use(matplotx.styles.dufte)

@dataclass
class VizData:
    title: str
    ylabel: str
    xlabel: str
    df: DataFrame

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

jobs_industry = jobs.filter(pl.col('Category') == 'Jobs by industry').sort('Year')
jobs_industry = jobs_industry.filter(pl.col('Industry Space Use') != 'Total jobs')
jobs_industry = jobs_industry.filter(pl.col('Geography').is_in(['Melbourne (CBD)', 'Carlton', 'Kensington', 'Parkville', 'South Yarra', 'Southbank']))
jobs_industry['Industry Space Use'].unique()
jobs_industry['Geography'].unique()
jobs_industry


# Ranks for Finance and insurance industry
finance_ranks = jobs_industry.filter(pl.col('Industry Space Use') == 'Finance and insurance').filter(pl.col('Year') <= 2035).with_columns(pl.col('Value').rank().alias('Rank')).sort('Rank', descending=True)
finance_ranks[['Geography', 'Year', 'Rank']]

# Ranks for Health care and social assistance industry
healthcare_ranks = jobs_industry.filter(pl.col('Industry Space Use') == 'Health care and social assistance').filter(pl.col('Year') <= 2035).with_columns(pl.col('Value').rank().alias('Rank')).sort('Rank', descending=False)

# Ranks for Education and training industry
education_ranks = jobs_industry.filter(pl.col('Industry Space Use') == 'Education and training').filter(pl.col('Year') <= 2035).with_columns(pl.col('Value').rank().alias('Rank')).sort('Rank', descending=False)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the ranks
ax.plot(finance_ranks['Rank'], label='Finance and insurance')
# ax.plot(healthcare_ranks['Rank'], label='Health care and social assistance')
# ax.plot(education_ranks['Rank'], label='Education and training')

# Set axis labels and title
ax.set_xlabel('Rank')
ax.set_ylabel('Value')
ax.set_title('Ranks of Industries')

# Add a legend
ax.legend()

# Show the plot
plt.show()