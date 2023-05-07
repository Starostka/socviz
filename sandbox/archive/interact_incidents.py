import polars as pl
import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show
from bokeh.sampledata.commits import data
from bokeh.transform import jitter
from bokeh.palettes import HighContrast3
from bokeh.plotting import figure, show
from bokeh.io import show
from bokeh.layouts import row
from bokeh.models import CustomJS, RadioButtonGroup
from bokeh.models import TabPanel, Tabs
from bokeh.plotting import figure, show
from sandbox.preprocess import preprocess_dataset1
dataset = preprocess_dataset1(print_schema=True)


DAYS = list(dataset['DayOfWeek'].unique())
LABELS = ["ROBBERY", "WARRANTS"]
YEARS = [2016, 2017, 2018]
DISTRICTS = ['SOUTHERN', 'TENDERLOIN']
dataset.schema
data = (
    dataset
    .filter(pl.col('Category').is_in(LABELS))
    # .filter(pl.col('year') > 2015)
    # .groupby('Category')
    # .agg([pl.col('count'), pl.col('year').flatten(), pl.col('Date').flatten()])
    # .explode('year').explode('count')
    .select(['Category', 'Time', 'Date'])
)
source = ColumnDataSource(data.to_pandas())

p = figure(width=800, height=300, y_range=LABELS, x_axis_type='datetime',
           title="Incidents by Year")

p.scatter(x='Time',
    y=jitter('Date', width=0.5, range=p.y_range),  source=source, alpha=0.2)

p.xaxis.formatter.days = '%Hh'
p.x_range.range_padding = 0
p.ygrid.grid_line_color = None
show(p)


# please create an interactive bokeh plot that plots 