import polars as pl
import plotly.express as px
from sandbox.preprocess import preprocess_dataset1
dataset = preprocess_dataset1(print_schema=True)
dataset.schema
dataset = dataset.drop_nulls()

# rolling window mean incident count for each year
data = (
    dataset
    .sort(pl.col('Date'))
    .filter(pl.col('Category') == 'ROBBERY')
    .groupby_dynamic("Date", every="1y")
    .agg(pl.count())
)
# data = dataset.filter(pl.col('Category') == 'ASSAULT').groupby(pl.col('Date').dt.year().sort()).agg(pl.count())
data = data.drop_nulls()
data = data.to_pandas()

fig = px.bar(data, x='Date', y='count')
fig.show()

# Finally to reflect on how robbery has changed troughut the year we compute the rolling window of robbery incidents 
# Finally we count the incident count for each year 

# data = dataset.sort(pl.col('Date')).filter(pl.col('Category').is_in(['ASSAULT', 'WEAPON LAWS']))#.groupby_dynamic("Date", every="1y").agg(pl.count())