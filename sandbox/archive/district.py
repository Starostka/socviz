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


tab1 = TabPanel(child=column(par1, p1), title="District 1")
tab2 = TabPanel(child=column(par2, p1), title="District 2")