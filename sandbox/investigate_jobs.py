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

jobs_industry = jobs.filter(pl.col('Category') == 'Jobs by industry')
jobs_space = jobs.filter(pl.col('Category') == 'Jobs by space use')

data = (jobs_industry
        .filter(pl.col('Industry Space Use') == 'Total jobs')
        .sort('Year')
        .groupby('Geography').agg([pl.col('Year'), pl.col('Value')]))

viz = VizData(title="Total jobs forecast, City of Melbourne", ylabel="Total jobs", xlabel="Year", df=data)
plt.bar(data['Year'], data['Value'])
#plt.plot(data['Year'], data['Value'])
plt.title(viz.title)
plt.ylabel(viz.ylabel)
plt.xlabel(viz.xlabel)
plt.show()


jobs_category = jobs.groupby('Category')
jobs.groupby('Category')

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
list(jobs['Geography'].unique())


list(unique_forecasts(jobs_industry))

# Geographical forecasts for various types
geo_forecast(jobs_industry, 'Total jobs').explode(['Year', 'Value']).filter(pl.col('Geography') == 'City of Melbourne')

geo_forecast(jobs_industry, 'Accommodation')
geo_forecast(jobs_industry, 'Education and training')
geo_forecast(jobs_industry, 'Health care and social assistance')
geo_forecast(jobs_industry, 'Finance and insurance')

jobs_industry



# == Investigating jobs by space use
list(unique_forecasts(jobs_space))

# Geographical forecasts for various types
geo_forecast(jobs_space, 'Total jobs')
geo_forecast(jobs_space, 'Accommodation - Commercial')
geo_forecast(jobs_space, 'Education')

# == visualizations

def plot(data:VizData, show=False, save_fig=False):
    # plt.figure(figsize=(100,10), dpi=600)
    plt.bar(data.df['Year'], data.df['Value'])

    plt.title(data.title)
    plt.ylabel(data.ylabel)
    plt.xlabel(data.xlabel)
    # plt.xticks(data.df['Year'])
    
    if save_fig:
        plt.savefig('output/nn_classification_accuracy.svg')
    
    if show:
        plt.show()

data = geo_forecast(jobs_industry, 'Education and training').explode(['Year', 'Value']).filter(pl.col('Geography') == 'City of Melbourne')
data = VizData(title="Education and training forecast, City of Melbourne", ylabel="Education & training", xlabel="Year", df=data)
plot(data, True)

data = geo_forecast(jobs_space, 'Total jobs').explode(['Year', 'Value']).filter(pl.col('Geography') == 'City of Melbourne')
data = VizData(title="Total jobs forecast, City of Melbourne", ylabel="Total jobs", xlabel="Year", df=data)
plot(data, True)

data = geo_forecast(jobs_space, 'Total jobs').explode(['Year', 'Value']).filter(pl.col('Geography') == 'City of Melbourne')
data = VizData(title="Total jobs forecast, City of Melbourne", ylabel="Total jobs", xlabel="Year", df=data)
plot(data, True)


data = jobs_industry.groupby('Industry Space Use').agg(pl.sum('Value')).sort('Value', reverse=True)[1:].limit(6)
list(data['Industry Space Use'])

data.filter(pl.col('Industry Space Use').is_in(['Finance and insurance', 'Health care and social assistance', 'Education and training']))
viz = VizData(title="Industry comparison, job forecast", ylabel="Jobs", xlabel="Industry", df=data)
plt.bar(data['Industry Space Use'], data['Value'])
plt.title(viz.title)
plt.ylabel(viz.ylabel)
plt.xlabel(viz.xlabel)
plt.show()


# mean change by region for industries
# 'Finance and insurance', 'Health care and social assistance', 'Education and training'
# With the City of Melbourne having a mean change in jobs for the 3 mentioned industries. being having a mean the region with the 

# == Investigation into industries and areas of Melbourne

# We can quickly inspect what areas and industries have the steadiest trend in the jobs forecast from the mean value
jobs_industry.groupby(['Geography', 'Industry Space Use'], maintain_order=True).agg([pl.col('Value').mean()]).sort('Value', reverse=True).limit(8)


# Computing the total job forecasts for specifically finance, health and education
q = (jobs_industry
 .filter(pl.col('Industry Space Use')
         .is_in(['Finance and insurance', 'Health care and social assistance', 'Education and training']))
    .groupby(['Geography', 'Industry Space Use'], maintain_order=True).agg([pl.col('Value').sum()]))
q

# Plot job forecasting lines for City of Melbourne
#TODO (jobs_industry)

# Plotting the total jobs across areas and industries
data = geo_forecast(jobs_industry, 'Total jobs').explode(['Year', 'Value']).filter(pl.col('Geography') == 'City of Melbourne')
viz = VizData(title="Total jobs forecast, City of Melbourne", ylabel="Total jobs", xlabel="Year", df=data)
plot(viz, True)
# In the coming years the city of Melbourne is expected to see a steady and substantial increase in the jobs available across different industries.

# With a growth rate being suffered in industries: TODO and bettered in industries: TODO

# TODO include growth rate across industries

# Plotting the total jobs with a rolling window to see years with potential fluctuations
# TODO do a rolling window here

# Loading historical data on available jobs
# src: https://app.remplan.com.au/melbourne-lga/economy/trends/jobs?state=GLZrFN!az4VClkNKSYeGD6Uvqea6f0c4I6ZouPIWIKJhGI8hxx7AUwzL
jobs_historic = pl.read_csv('data/melbourne-jobs-historically.csv', separator=';')
jobs_historic.schema
jobs_historic.sort('2021', reverse=True)
# Historically considering data from 2016 and 2021 employment in the space of (Professional, Scientific and Technical Services) and (Financial and Insurance Services)
# have had the biggest number of jobs. This is reinforced by the forecast that again indicates an increase of jobs for these industries.
# Overall Melbourne can be consiered a modern societry that have the resoruces need to priotise education and economical growth.

# Loading the gross regional product
# src: https://app.remplan.com.au/melbourne-lga/economy/industries/gross-regional-product?state=5wPkHA!9pXzH09r5i9bJY5CKd1a9SrTKI3k0FeIvI9U4Iezx
grp = pl.read_csv('data/melbourne-grp.csv', separator=';').to_pandas()
grp = grp.replace({'\$': '', '\.': '', 'US': ''}, regex=True)
grp = pl.from_pandas(grp)
grp.schema
grp.columns
grp

# So we can rank the different areas with respect to health, finance and education respectively starting with forecast towards 2025
jobs_industry.filter(pl.col('Industry Space Use') == 'Finance and insurance').filter(pl.col('Year') <= 2025).with_columns(pl.col('Value').rank('min').alias('Rank')).sort('Rank', reverse=True)
jobs_industry.filter(pl.col('Industry Space Use') == 'Health care and social assistance').filter(pl.col('Year') <= 2025).with_columns(pl.col('Value').rank().alias('Rank')).sort('Rank', reverse=True)
jobs_industry.filter(pl.col('Industry Space Use') == 'Education and training').filter(pl.col('Year') <= 2025).with_columns(pl.col('Value').rank().alias('Rank')).sort('Rank', reverse=True)

# Next we will how they stand towards 2035, a change in 10 years.
jobs_industry.filter(pl.col('Industry Space Use') == 'Finance and insurance').filter(pl.col('Year') <= 2035).with_columns(pl.col('Value').rank('min').alias('Rank')).sort('Rank', reverse=True)
jobs_industry.filter(pl.col('Industry Space Use') == 'Health care and social assistance').filter(pl.col('Year') <= 2035).with_columns(pl.col('Value').rank().alias('Rank')).sort('Rank', reverse=True)
jobs_industry.filter(pl.col('Industry Space Use') == 'Education and training').filter(pl.col('Year') <= 2035).with_columns(pl.col('Value').rank().alias('Rank')).sort('Rank', reverse=True)


q.sort('Value', reverse=False).limit(8)
# If we take a look at the forecasted amount of jobs for the various regions in Melbourne we see that South Yarra and Parkville
# is among some of the least progressive in terms of future jobs. South Yarra has a history of being and attractive to live in
# with good proximity to CBD, schools, transportations and open lush parks and spaces (https://en.wikipedia.org/wiki/South_Yarra).
# It is also located right next to Toorak which is famous for its luxury residence and entreprenurs living there (https://en.wikipedia.org/wiki/Toorak,_Victoria).

# Since these surburbs mainly consist of businesses such as restaurants and cafes
# are the ones available here, they don't see a lot of change in jobs for finance, health and education.
# These types of industries are located closer to the CBD.

q.sort('Value', reverse=True).limit(8)
# As we can see the CBD of Melbourne is expected to see a huge increase the coming years with in jobs more specifically for finance and insurance.
# In terms of jobs in health care and social assistance services the Parkville suburb will see a big incease.
# Parkville houses one of Australia's top hospitals both in its specializations but also as a teaching hospital.
# And since the general trend seems to favour more education this is likely to be correlated.  



# == End of investigation into industries and areas of Melbourne

# The City of Melbourne shows the most pregression for all the 3 mentioned industries. Showing that 


jobs_industry['Geography'].unique()

# correlation between industry type for same region
first = (jobs_industry
 .filter(pl.col('Geography') == 'Docklands')
 .filter(pl.col('Industry Space Use') == 'Finance and insurance')
 .sort('Year'))

second = (jobs_industry
 .filter(pl.col('Geography') == 'Docklands')
 .filter(pl.col('Industry Space Use') == 'Health care and social assistance')
 .sort('Year'))

res = stats.pearsonr(first['Value'], second['Value'])
res.confidence_interval()
res

# correlation between regions for same industry type
first = (jobs_industry
 .filter(pl.col('Geography') == 'Docklands')
 .filter(pl.col('Industry Space Use') == 'Finance and insurance')
 .sort('Year'))

second = (jobs_industry
 .filter(pl.col('Geography') == 'Carlton')
 .filter(pl.col('Industry Space Use') == 'Finance and insurance')
 .sort('Year'))

res = stats.pearsonr(first['Value'], second['Value'])
res.confidence_interval()
res
