import polars as pl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pathlib
from dataclasses import dataclass
from functools import partial, singledispatch

path: pathlib.Path = 'data/Police_Department_Incident_Reports__Historical_2003_to_May_2018.csv'
data1 = pl.scan_csv(path).collect()

path: pathlib.Path = 'data/Police_Department_Incident_Reports__2018_to_Present.csv'
data2 = pl.scan_csv(path).collect()

def correct_time(dataframe):
    return dataframe.with_columns(
        pl.col('Time').str.strptime(
            datatype = pl.Time,
            fmt='%H:%M'
        )
    )

data1 = correct_time(data1)
data2 = correct_time(data2)

# == summary statistics dataset 1 ==

# number of entries in each category
data1.groupby(pl.col('Category')).agg(pl.count())
data1.groupby(pl.col('Category')).agg(pl.count()).to_numpy()

# median for time of incident for each category
data1.groupby(pl.col('Category')).agg(pl.col('Time').median()).to_numpy()

# == summary statistics dataset 2 ==

# number of entries in each category
data2.groupby(pl.col('Category')).agg(pl.count()).to_numpy()

# median for time of incident for each category
data2.groupby(pl.col('Category')).agg(pl.col('Time').median()).to_numpy()
