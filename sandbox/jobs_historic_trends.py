import plotly.graph_objects as go
import polars as pl
import numpy as np

jobs_historic = pl.read_csv('data/melbourne-jobs-historically.csv', separator=';')
q = jobs_historic.sort('2021', descending=False)
q.filter(pl.col('Options').is_in(['Professional, Scientific and Technical Services',
                         'Financial and Insurance Services',
                         'Education and Training',
                         'Health Care and Social Assistance',
                         'Accommodation and Food Services']))

fig = go.Figure()
fig.add_trace(go.Bar(
    y=q['Options'],
    x=q['2021'],
    error_x=dict(type='data', array=q['2021'] - q['2016']),
    orientation='h'
))

fig.update_layout(
    title='Employments back in 2016 and 2021',
    xaxis_title='Employments',
    yaxis_title=None,
    yaxis=dict(autorange='reversed')
)

fig.show()