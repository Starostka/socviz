import polars as pl

data = pl.read_csv("data/super-sunday-bike-count.csv")
data.head().collect()

data.columns


data.collect().describe()
data.schema


data = (
    pl.read_csv("data/super-sunday-bike-count.csv").lazy()
    .with_columns(['state', 'electorate', 'bicycle', 'walker', 'runner', 'dog', 'other', 'total'])
).collect()

data['bicycle']

len(data.columns)
data['year'].unique()

data['state']

data.groupby(['site_id']).agg(pl.count())
