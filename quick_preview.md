---
title: SF Crime Data Analysis and Visualization
subtitle: 02806 Assignment 2 
---

```{python}
import folium
import pandas as pd
import polars as pl
import pandas as pd
from bokeh.io import output_notebook
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
from bokeh.models import Paragraph
from folium.plugins import HeatMap
```

# Introduction

San Francisco is a well-know metropolis, as the commercial, financial and cultural center of North California in the USA, it has attracted a massive amount of people migrated and lived in the city. With 815,201 residents [up to 2021](https://fred.stlouisfed.org/series/CASANF0POP), the diverse population has made impactful contribution to the economic of San Francisco. However, the wide range of socioeconomic challenges in San Francisco also contributes to the high crime rate. 

## Dataset
In this story, we will explore the San Francisco Police Department's (SFPD) [Incient Report Dataset](https://data.sfgov.org/browse?category=Public+Safety) with the time frame from January 2003 to May 2018.

This dataset is a collection of data on criminal incidents reported in SF, which provides the information of `incident date`, `incident time`, `incident category`, `police district`, `latitude`, `logitude`, etc. The dataset contains 35 columns and more than 2 million records of crimes within the timeframe. According to the data, there were 37 categories of crimes recorded across San Francisco city. 

## Abstract
The aim of this report is utilizing the techniques of data visualization for the analytics of crime occured in San Francisco. The primary idea of this data analysis study is to obtain the insights from the observation, in order to evaluate the criminal situation for the past decades in San Francisco, as well as help prevent potential crimes in the future. The data analysis will be based on **Time-Series**, **Geographic** and **Interative Visualization** respectively.

According to [SFNext Index](https://www.sfchronicle.com/projects/2022/fixing-san-francisco-problems/crime), with the exception of robberies, violent crime in San Francisco is below average for large cities. In 2019 and 2020, San Francisco ranked in the bottom half among major U.S. cities, with rates of 670 and 540 violent crime incidents per 100,000 residents, respectively. Hence, we are interested in how `Robbery` had increased the violent crime level in San Francisco. 

# Data Anlysis: Robberies in San Francisco
From January 2003 to December 2012, there were 35817 incidents of robbery in San Francisco reported to the police, while there were 32786 incidents of robbery reported from 2013 to 2022 [(Data source)](https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-2018-to-Present/wg3w-h783). As an overview, the robbery rate has decreased by 8.5% since the decade of 2003 to the last decade, however the number is not indicating a significantly decrease, which reflects the robbery is still a key factor that affect the level of crimes in San Francisco.

## Timeseries: How the occurrence of Robbery changed over the time?
<!--  One time-series / bar chart (it's OK to use the "fancy" plot-typs like calendar plots or polar bar-charts from Week 2, Part 4). -->

If we divide the time of the incidents into hourly timeslots, it becomes apparent that the number of robberies reaches its highest point between 2 and 3 pm and remains consistently high until 5 pm. After 5 pm, there is a sharp decline during the evening, but a secondary peak occurs between 1 and 2 am.Between 2 am and 2 pm, the number of incidents increases steadily. 

```{python}
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


df_before_2018 = pd.read_csv('../Police_Department_Incident_Reports__Historical_2003_to_May_2018.csv')
df_before_2018['Date'] = pd.to_datetime(df_before_2018['Date'])
df_before_2018['Year'] = df_before_2018['Date'].dt.year
df_before_2018['Month'] = df_before_2018['Date'].dt.month
df_before_2018['Hour'] = pd.DatetimeIndex(df_before_2018['Time']).hour
df_before_2018 = df_before_2018.loc[df_before_2018['Year'] != 2018]


focuscrimes = ['ROBBERY']

hour_of_day = [i for i in range(0,24)]
hourly_slots = {}
for i in range(len(hour_of_day)):
    if i+1 == len(hour_of_day):
        start = hour_of_day[i]
        end = hour_of_day[0]
        hourly_slots[start] = str(start) + "-" + str(end)
    else:
        start = hour_of_day[i]
        end = hour_of_day[i+1]
        hourly_slots[start] = str(start) + "-" + str(end)

df_before_2018["time_period"] = [hourly_slots[int(str(i).split(":")[0])] for i in list(df_before_2018['Hour'])]

yearly_pattern = df_before_2018.groupby(by=["Year", "Category"]).size().reset_index(name="Count")

yearly_pattern = yearly_pattern.loc[yearly_pattern['Category'].isin(focuscrimes)].reset_index(drop=True)

hourly_pattern = df_before_2018.groupby(by=["time_period", "Category"]).size().reset_index(name="Count")

hourly_pattern = hourly_pattern.loc[hourly_pattern['Category'].isin(focuscrimes)].reset_index(drop=True)


plt.figure(figsize=(7.5,5))
plt.suptitle("Robbery Incidents in Time-series" ,fontsize=14, y=1.0, fontweight='bold', color='black')

# Yealy trend
temp1 = yearly_pattern.loc[yearly_pattern['Category'] == 'ROBBERY'].reset_index(drop=True)
x = temp1["Year"]
y = temp1["Count"]
plt.subplot(2,2,1)
plt.title('Robbery Incidents Yealy Pattern', pad=-14, fontsize = 9, fontweight='bold', fontstyle="italic")
plt.bar(x, y, width=0.6, edgecolor="black", color='lavender')
plt.xticks(x, yearly_pattern['Year'].unique().tolist(), rotation=45, fontsize = 7)
plt.tight_layout()
plt.ylim(top=(np.max(y)+(np.max(y)*0.3)))

# Hourly trend
temp2 = hourly_pattern.loc[hourly_pattern['Category'] == 'ROBBERY'].reset_index(drop=True)
x = temp2["time_period"]
y = temp2["Count"]
plt.subplot(2,2,2)
plt.title('Robbery Incidents Hourly Pattern', pad=-14, fontsize = 9, fontweight='bold', fontstyle="italic")
plt.bar(x, y, width=0.6, edgecolor="black", color='lavender')
plt.xticks(x, hourly_slots.values(), rotation=45, fontsize = 6)
plt.tight_layout()
plt.ylim(top=(np.max(y)+(np.max(y)*0.3)))

# Calplot
img = mpimg.imread('Calplot_2012.png')
plt.subplot(2,1,2)
plt.imshow(img)
plt.axis('off')

plt.tight_layout()
```

From 2003 to 2017, we can see the incidents fluctuated accross years. Specifically, in 2010 and 2011, it has a significant decreased from 2008 and 2009. The [Rand Corporation](https://www.rand.org/) studied this phenomenon on a national level in 2010, concluding that the crime prevention benefit of hiring more officers is well worth the cost. [Reference](https://countyda.sccgov.org/sites/g/files/exjcpb1121/files/10-Year%20Combined%20CA%20Crime%20Stat%20Report.pdf)

However, there was a resurgence in incidents in 2012, with a noticeable gap from the previous year. After analyzing the robbery incidents data in 2012, we observed a marked increase in robberies on the final Sunday in June in San Francisco. Further investigation revealed that this date coincided with the San Francisco LGBT Pride Parade, which started at Beale Street and Market Street and continued down to 8th Street.

<!-- put the plot here -->

## Map: Where does robbery most likely take place?
<!-- One map (use techniques from Week 3 and 4) -->
Let's examine the robbery locations on June 24, 2012, during the Pride Parade in San Francisco which typically occurs on Market Street[(Reference: Wikipedia)](https://en.wikipedia.org/wiki/San_Francisco_Pride#:~:text=The%20San%20Francisco%20Pride%20parade,until%20almost%204%3A00%20pm.).

In the visualization of the robbery incidents data on the day when the Pride Parade occured, the three location marks Market Street, 8th Street and Beala Street respectively. The red dots indicates the location of the robberies taking place. It shows an obvious fact that in the 33 incidents recorded on 24 June 2012, most of the crimes happened in the range of the routes that the parade covered. 

<!-- put the map here -->
```{python}
# df_before_2018 = pd.read_csv('../Police_Department_Incident_Reports__Historical_2003_to_May_2018.csv')
# df_before_2018['Date'] = pd.to_datetime(df_before_2018['Date'])
# df_before_2018['Year'] = df_before_2018['Date'].dt.year
# df_before_2018['Month'] = df_before_2018['Date'].dt.month
# df_before_2018['Hour'] = pd.DatetimeIndex(df_before_2018['Time']).hour
# df_before_2018 = df_before_2018.loc[df_before_2018['Year'] != 2018]

# << uses pre-transformed instead of above
df_before_2018 = pl.read_csv('data/before_2018.csv').to_pandas()

df_robbery = df_before_2018.loc[df_before_2018['Category']=="ROBBERY"]
df_robbery = df_robbery[df_robbery["Year"] == 2012]
df_robbery_pride = df_robbery[df_robbery['Date'] == '2012-6-24']

SF_map = folium.plugins.DualMap(location=[37.77919, -122.41914],
                    zoom_start = 12,
                    tiles = "openstreetmap")

constraint = (df_before_2018['Category'] == 'ROBBERY') & (df_before_2018['Year'] >= 2011) & (df_before_2018['Year'] <= 2012) & (df_before_2018['Resolution'] == "ARREST, BOOKED")
df_robbery_heat = df_before_2018.loc[constraint].reset_index(drop=True)


get_XY = list(zip(list(df_robbery_pride["Y"]), list(df_robbery_pride["X"])))

SF_map = folium.Map([37.77919, -122.41914], zoom_start=13, tiles = "openstreetmap")
folium.Marker([37.77351584799628, -122.42148577465927], popup="Market Street").add_to(SF_map)
folium.Marker([37.78907067508782, -122.3929690574588], popup="Beala Street").add_to(SF_map)
folium.Marker([37.77295458293956, -122.40701151351163], popup='8th Street').add_to(SF_map)

for x,y in get_XY:
    folium.CircleMarker([x, y],
                    radius=2,
                    color='red',
                    ).add_to(SF_map)


x_y_robbery = list(zip(list(df_robbery_heat["Y"]), list(df_robbery_heat["X"])))

HeatMap(x_y_robbery, min_opacity=0.35, overlay=True).add_to(SF_map)

SF_map
```

The incidence of robbery is relatively high in the near Market Street, indicating that criminals are more prone to commit robbery in crowded areas, thus increasing their chances of escape. Additionally, the buildings and blocks in the Market Street area are more densely packed, offering additional cover and refuge for criminals. 

This observation also aligns with the result of the heatmap regarding robbery occurrence in 2011 and 2012, as the map above indicates. It reveals the fact that areas with a high concentration of stores and a large population, along with a complex urban infrastructure, are more susceptible to robbery incidents.

However, despite the fact that the Tenderloin district where Market Street located had the highest number of robbery incidents, the data implies that it was not the most active police district. This fact can be counted to the assumption that there was a lack of police power resources in Tenderloin district.


## SOME HEADER ABOUT CATEGORIES


```{python}
# Configure for output in the notebook
output_notebook()

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
```

# Conclusion
As the analysis presented, we had investigated into the robbery incidents in San Francisco and put the focus on discussing the situation from 2008 to 2012 based on time series. Particularly, by looking into the calendar plots across 2003 to 2017, it briefly showed that the incidents of robbery usually peaks at summer time. By visualizing the incidents of robbery on the map, we could conclude that the busiest city center tend to be the place that crimes are more likely happen. However, the activities of police related to the districts does not show a positive correlation with the numbers of incidents. 