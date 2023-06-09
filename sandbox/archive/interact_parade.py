import folium
import pandas as pd
import polars as pl
import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show
from bokeh.sampledata.commits import data
from bokeh.transform import jitter
from bokeh.palettes import HighContrast3
from bokeh.plotting import figure, show
from bokeh.io import show
from bokeh.layouts import row, column
from bokeh.models import CustomJS, RadioButtonGroup
from bokeh.models import TabPanel, Tabs
from bokeh.plotting import figure, show
from bokeh.io import show
from bokeh.models import Paragraph
from bokeh.transform import dodge
from folium.plugins import HeatMap
# from sandbox.preprocess import preprocess_dataset1

# == generate files
# df_before_2018 = pd.read_csv('data/Police_Department_Incident_Reports__Historical_2003_to_May_2018.csv')
# df_before_2018['Date'] = pd.to_datetime(df_before_2018['Date'])
# df_before_2018['Year'] = df_before_2018['Date'].dt.year
# df_before_2018['Month'] = df_before_2018['Date'].dt.month
# df_before_2018['Hour'] = pd.DatetimeIndex(df_before_2018['Time']).hour
# df_before_2018 = df_before_2018.loc[df_before_2018['Year'] != 2018]
# df_robbery = df_before_2018.loc[df_before_2018['Category']=="ROBBERY"]
# df_robbery = df_robbery[df_robbery["Year"] == 2012]
# df_robbery_pride = df_robbery[df_robbery['Date'] == '2012-6-24']
# get_XY = list(zip(list(df_robbery_pride["Y"]), list(df_robbery_pride["X"])))
# dir(df_before_2018)
# df_before_2018.to_csv('data/before_2018.csv')

dataset = pl.read_csv('data/before_2018.csv')

data = (
    dataset
    .filter(pl.col('Category') == 'ROBBERY')
    .groupby('Year').agg(pl.count())
).to_pandas()
p1 = figure(width=600, height=300, title="Robbery incidents")
p1.xgrid.grid_line_color = None
p1.xaxis.ticker = sorted(data['Year'].to_list())
p1.vbar(x=data['Year'], top=data['count'], width=0.9, alpha=0.4)
par1 = Paragraph(text=f"""
    Mean incident count: {data['count'].mean():3.2f}
    """,
    width=600, height=50)
tab2 = TabPanel(child=p2, title="ROBBERY")


data = (
    dataset
    .filter(pl.col('Category') == 'WARRANTS')
    .groupby('Year').agg(pl.count())
).to_pandas()
p2 = figure(width=600, height=300, title="Warrant incidents")
p2.xgrid.grid_line_color = None
p2.xaxis.ticker = sorted(data['Year'].to_list())
p2.vbar(x=data['Year'], top=data['count'], width=0.9, alpha=0.4)
par2 = Paragraph(text=f"""
    Mean incident count: {data['count'].mean():3.2f}
    """,
    width=600, height=50)
show(p2)

tabs = TabPanel(child=column(par2, p1), title="WARRANTS")
show()

par1 = Paragraph(text=f"""
    Mean incident count: {data['count'].mean():3.2f}
    """,
    width=600, height=50)
tab1 = TabPanel(child=column(par1, p1), title="ROBBERY")

data = (
    dataset
    .filter(pl.col('Category') == 'ROBBERY')
    .groupby('Year').agg(pl.count())
).to_pandas()
p1 = figure(width=600, height=300, title="Robbery incidents")
p1.xgrid.grid_line_color = None
p1.xaxis.ticker = sorted(data['Year'].to_list())
p1.vbar(x=data['Year'], top=data['count'], width=0.9, alpha=0.4)
par2 = Paragraph(text=f"""
    Mean incident count: {data['count'].mean():3.2f}
    """,
    width=600, height=50)
tab2 = TabPanel(child=column(par2, p1), title="WARRANTS")
show(Tabs(tabs=[tab1, tab2]))



data = (
    dataset
    .filter(pl.col('Category').is_in(['ROBBERY', 'WARRANTS']))
    .filter(pl.col('Year').is_in([2015, 2016, 2017]))
    .groupby(['Category', 'Year']).agg(pl.count().alias('Count'))
)
d1 = data.filter(pl.col('Category') == 'ROBBERY').to_pandas()
d2 = data.filter(pl.col('Category') == 'WARRANTS').to_pandas()

CATEGORIES = ['ROBBERY', 'WARRANTS']
p = figure(x_range=CATEGORIES, y_range=(0, 7000), title="Incident count per year",
           height=350, toolbar_location=None, tools="")
p.vbar(x=dodge('Category', 0.0, range=p.x_range), top='Count', source = d1,
       width=0.2, color="#c9d9d3", legend_label="2015")

p.vbar(x=dodge('Category',  0.0,  range=p.x_range), top='Count', source = d2,
       width=0.2, color="#718dbf", legend_label="2016")

p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"
show(p)