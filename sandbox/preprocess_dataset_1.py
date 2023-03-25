import polars as pl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pathlib
from dataclasses import dataclass
from functools import partial, singledispatch

path: pathlib.Path = 'data/Police_Department_Incident_Reports__Historical_2003_to_May_2018.csv'
dataset = pl.scan_csv(path, try_parse_dates=True).collect()

dataset.schema

dataset = dataset.with_columns(
    [
        pl.col('Time').str.strptime(
            datatype = pl.Time,
            fmt='%H:%M'
        ),
        pl.col('Category').cast(pl.Categorical())
    ]
)

# TODO: remove columns not needed and prefixes "DELETE - " 