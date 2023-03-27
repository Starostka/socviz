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
from folium.plugins import HeatMap
from sandbox.preprocess import preprocess_dataset1

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

dataset = pl.read_csv('before_2018.csv')

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
tab1 = TabPanel(child=column(par1, p1), title="ROBBERY")

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
tab2 = TabPanel(child=column(par2, p1), title="WARRANTS")

show(Tabs(tabs=[tab1, tab2]))