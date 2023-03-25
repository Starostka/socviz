import polars as pl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pathlib
from dataclasses import dataclass
from functools import partial, singledispatch

path: pathlib.Path = 'data/Police_Department_Incident_Reports__2018_to_Present.csv'
dataset = pl.scan_csv(path, try_parse_dates=True, ignore_errors=True).collect()

dataset.schema

dataset = dataset.with_columns(
    [
        pl.col('Incident Date').alias('Date'),
        pl.col('Incident Year').alias('Year'),
        pl.col('Incident Time').str.strptime(
            datatype = pl.Time,
            fmt='%H:%M'
        ).alias('Time'),
        pl.col('Category').cast(pl.Categorical())
    ]
)