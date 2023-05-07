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
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure, show
from bokeh.io import show
from bokeh.palettes import Category20

dataset = pl.read_csv('data/before_2018.csv')
data = (
    dataset
    .groupby(['Hour', 'PdDistrict']).agg(pl.count())
    .with_columns((pl.col('Hour')/pl.col('count')).alias('normalized'))
    .sort(pl.col('Hour'))
)
data = data.pivot(index = 'Hour', columns = ['PdDistrict'], values = ['normalized'])
# data.schema

focuscrimes = set(['BAYVIEW', 'INGLESIDE', 'TARAVAL', 'CENTRAL'])

source = ColumnDataSource(data.to_pandas())
hours = data['Hour'].unique().to_list()
hours = sorted(hours)
p = figure(title="Crimes per hour", x_axis_label='Hour of the day', y_axis_label='Percentage Frequency', 
           x_range = FactorRange(factors=[str(hour) for hour in hours]))
bar = {}
for indx, i in enumerate(focuscrimes):
    bar[i] = p.vbar(x="Hour", top=i, width=0.3, 
                    source=source, legend_label=i, muted_alpha=0.2, muted=False, color=Category20[14][indx])
p.legend.title = "Category"
p.legend.location = "top_left"

p.legend.click_policy = "hide"
p.legend.label_text_color = "black"
p.legend.title_text_color = "black"
show(p)






df = pd.read_csv('data/before_2018.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df = df[df.Year >= 2010].reset_index(drop=True)
df = df[df.Year < 2018].reset_index(drop=True)
df['Hour'] = pd.DatetimeIndex(df['Time']).hour
hourly_pattern = df.groupby(by=["Hour", "PdDistrict"]).size().reset_index(name="Occurence")
hourly_pattern = hourly_pattern.loc[hourly_pattern['PdDistrict'].isin(focuscrimes)].reset_index(drop=True)
category = hourly_pattern['PdDistrict'].unique().tolist()
hourly_pattern['Sum'] = hourly_pattern.groupby('PdDistrict')['Occurence'].transform('sum')
hourly_pattern['Norm'] = hourly_pattern['Occurence'] / hourly_pattern['Sum']
hourly_pattern = hourly_pattern.pivot_table(index='Hour', columns='PdDistrict', values='Norm')
hourly_pattern






src = ColumnDataSource(data.to_pandas())
p = figure(x_range = FactorRange(factors=data['Hour'].unique()), title="Department district - Performance") 

bar = {}
for idx, row in enumerate(data.rows(named=True)):
    print(row)
    break


    bar[row['']] = p.vbar(x='Hour',  top=i, source=src,
        legend_label=i,  alpha=0.7) 