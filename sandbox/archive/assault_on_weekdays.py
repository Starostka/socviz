import polars as pl
import pandas as pd
import numpy as np
import pathlib
from dataclasses import dataclass
from functools import partial, singledispatch

path: pathlib.Path = 'data/Police_Department_Incident_Reports__Historical_2003_to_May_2018.csv'
data1 = pl.scan_csv(path).collect()

path: pathlib.Path = 'data/Police_Department_Incident_Reports__2018_to_Present.csv'
data2 = pl.scan_csv(path).collect()

data1['Category'].unique()

q = (
    data1.lazy()
    .filter(pl.col('Category') == 'ASSAULT')
    .groupby('DayOfWeek')
    .agg(pl.count())
).collect()

# tufte inspired plot
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Gobal options.
plt.rcParams['font.family'] = 'serif'

# Plot the bars.
fig, ax = plt.subplots()

labels = q[:,0]
x = list(range(len(labels)))
y = q[:,1]

ax.bar(x, y, color='#7a7a7a', width=0.6)

# Remove axis lines.
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Add labels to x axis.
ax.set_xticks(x)
ax.set_xticklabels(labels)

# Add labels to y axis.
y_ticks = [5, 10, 15]
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_ticks)
ax.yaxis.set_major_formatter(ticker.PercentFormatter(decimals=0))

# Remove tick marks.
ax.tick_params(
    bottom=False,
    left=False, 
)

# Add bar lines as a horizontal grid.
ax.yaxis.grid(color='white')