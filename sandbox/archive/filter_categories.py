# create a plotly express plot that allows the user to turn on and off different combinations of groups in a dataset

import polars as pl
from sandbox.preprocess import preprocess_dataset1
dataset = preprocess_dataset1(print_schema=True)

