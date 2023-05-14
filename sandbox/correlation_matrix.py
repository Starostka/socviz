## Benjamin
# Correlation between jobs and population forecast

import polars as pl
import matplotlib.pyplot as plt
import matplotx
import seaborn as sns
plt.style.use(matplotx.styles.dufte)

jobs = pl.read_csv('data/jobs_forecast.csv', ignore_errors=True, try_parse_dates=True)
jobs_industry = jobs.filter(pl.col('Category') == 'Jobs by industry').sort('Year')
set(jobs_industry['Industry Space Use'].unique())
jobs_industry = jobs_industry.filter(pl.col('Geography') == 'City of Melbourne')
# jobs_industry = jobs_industry.filter(pl.col('Industry Space Use') == 'Education and training')
# jobs_industry = jobs_industry.filter(pl.col('Industry Space Use') == 'Finance and insurance')
jobs_industry = jobs_industry.filter(pl.col('Industry Space Use').is_in(['Finance and insurance', 'Education and training']))
jobs_industry.groupby([pl.col('Industry Space Use'), pl.col('Year')]).agg(pl.sum('Value'))

population = pl.read_csv('data/population_forecast.csv', ignore_errors=True, try_parse_dates=True)
population = population.filter(pl.col('Geography') == 'City of Melbourne')
population = population.filter(pl.col('Gender') != 'Not applicable')
population = population.filter(pl.col('Gender') != 'Total')
population = population.filter(pl.col('Age') != 'Average age')
population.groupby([pl.col('Gender'), pl.col('Age')]).agg(pl.sum('Value'))
population

# population['Age'].unique()
# population['Year'].max()

joined = jobs_industry.join(population, on='Year', suffix='_population')
joined = joined.rename({"Value": "Jobs", "Value_population": "Population"})

joined.with_columns(
    [(pl.col('Industry Space Use') == 'Finance and insurance').count().alias('Jobs Finance'),
     (pl.col('Industry Space Use') == 'Education and training').count().alias('Jobs Education')])

corr = joined[['Year', 'Jobs', 'Population']]

f, ax = plt.subplots(figsize=(8, 5))

sns.heatmap(corr[['Year', 'Jobs', 'Population']].corr(), annot=True)

plt.title('Correlation matrix', size=12)
ax.set_xticklabels(list(corr[['Year', 'Jobs', 'Population']].columns), size=12, rotation=90)
ax.set_yticklabels(list(corr[['Year', 'Jobs', 'Population']].columns), size=12, rotation=0)
plt.show()
