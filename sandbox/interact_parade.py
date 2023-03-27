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

data = (
    # dataset.
)

# == plot

p = Paragraph(text=f"""
    Description: {metadata.description}
    Median hour: {metadata.hour_median}
    """,
    width=200, height=100)

show(p)
