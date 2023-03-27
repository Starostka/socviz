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
from bokeh.models import Paragraph
from sandbox.preprocess import preprocess_dataset1
dataset = preprocess_dataset1(print_schema=True)




code_count = codes.pivot(index = 'Incident Code', values = ['count'], columns = ['PdDistrict'])

entry1 = code_count.filter(pl.col('Incident Code') == 63010)
p1 = figure(x_range=DISTRICTS, height=250, title="Department Units",
    toolbar_location=None, tools="hover", tooltips="$name @DISTRICTS: @$name")
p1.vbar(x = DISTRICTS, top = entry1['SOUTHERN'].to_list() + entry1['TENDERLOIN'].to_list(), width = 0.9,)
p1.y_range.start = 0
p1.x_range.range_padding = 0.2
p1.xgrid.grid_line_color = None
tab1 = TabPanel(child=p1, title="WARRANTS")
#show(Tabs(tabs=[tab1]))


entry2 = code_count.filter(pl.col('Incident Code') == 62050)
p2 = figure(x_range=DISTRICTS, height=250, title="Department Units",
    toolbar_location=None, tools="hover", tooltips="$name @DISTRICTS: @$name")
p2.vbar(x = DISTRICTS, top = entry2['SOUTHERN'].to_list() + entry2['TENDERLOIN'].to_list(), width = 0.9)
p2.y_range.start = 0
p2.x_range.range_padding = 0.2
p2.xgrid.grid_line_color = None
tab2 = TabPanel(child=p2, title="ROBBERY")

show(Tabs(tabs=[tab1, tab2, tab3]))


entry3 = code_count.filter(pl.col('Incident Code') == 4136)
p3 = figure(x_range=DISTRICTS, height=250, title="Department Units",
    toolbar_location=None, tools="hover", tooltips="$name @DISTRICTS: @$name")
p3.vbar(x = DISTRICTS, top = entry3['SOUTHERN'].to_list() + entry3['TENDERLOIN'].to_list(), width = 0.9)
p3.y_range.start = 0
p3.x_range.range_padding = 0.2
p3.xgrid.grid_line_color = None
tab3 = TabPanel(child=p3, title="ASSAULT")
p = Paragraph(text=f"""
    Description: {metadata.description}
    Median hour: {metadata.hour_median}
    """,
    width=200, height=100)

show(p)


show(Tabs(tabs=[tab1, tab2, tab3]))