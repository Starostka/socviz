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
from bokeh.io import show
from bokeh.models import Paragraph, ColumnDataSource, FactorRange


dataset = pl.read_csv('data/before_2018.csv')
cat_count = (dataset.groupby('Category').agg(pl.count()))

dataset = pl.read_csv('data/before_2018.csv')
data = (
    dataset
    .groupby(['Hour', 'PdDistrict']).agg(pl.count())
    .with_columns((pl.col('Hour')/pl.col('count')).alias('normalized'))
    .sort(pl.col('Hour'))
)
data = data.pivot(index = 'Hour', columns = ['PdDistrict'], values = ['normalized'])


p = figure(x_range = FactorRange(factors=data['Hour'].unique()), title="Department district - Performance") 

p1 = figure(width=600, height=300, title="Robbery incidents")

bar ={} # to store vbars
### here we will do a for loop:
for indx,i in enumerate(focuscrimes):
    bar[i] = p.vbar(x='name_of_the_column_that_contain_hours',  top=i, source= src, 
                    ### we will create a vbar for each focuscrime
                    legend_label=i,  muted_alpha=..., muted = ....) 