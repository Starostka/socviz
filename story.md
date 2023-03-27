---
title: Storyline
subtitle: Second assignment socviz
---

# Introduction

<!-- - TODO Explaining the dataset
- TODO abstract for the story
- TODO basic summary statistics/info for the dataset -->

San Francisco is a well-know metropolis, as the commercial, financial and cultural center of North California in the USA, it has attracted a massive amount of people migrated and lived in the city. With 815,201 residents [up to 2021](https://fred.stlouisfed.org/series/CASANF0POP), the diverse population has made impactful contribution to the economic of San Francisco. However, the wide range of socioeconomic challenges in San Francisco also contributes to the high crime rate. 

## Dataset
In this story, we will explore the San Francisco Police Department's (SFPD) [Incient Report Dataset](https://data.sfgov.org/browse?category=Public+Safety) with the time frame from January 2003 to May 2018.

This dataset is a collection of data on criminal incidents reported in SF, which provides the information of `incident date`, `incident time`, `incident category`, `police district`, `latitude`, `logitude`, etc. The dataset contains 35 columns and more than 2 million records of crimes within the timeframe. According to the data, there were 37 categories of crimes recorded across San Francisco city. 

## Abstract
The aim of this report is utilizing the techniques of data visualization for the analytics of crime occured in San Francisco. The primary idea of this data analysis study is to obtain the insights from the observation, in order to evaluate the criminal situation for the past decades in San Francisco, as well as help prevent potential crimes in the future. The data analysis will be based on **Time-Series**, **Geographic** and **Interative Visualization** respectively.

According to [SFNext Index](https://www.sfchronicle.com/projects/2022/fixing-san-francisco-problems/crime), with the exception of robberies, violent crime in San Francisco is below average for large cities. In 2019 and 2020, San Francisco ranked in the bottom half among major U.S. cities, with rates of 670 and 540 violent crime incidents per 100,000 residents, respectively. Hence, we are interested in how Robbery had increased the violent crime level in San Francisco. 

# Data Anlysis: Robberies in San Francisco
From January 2003 to December 2012, there were 35817 incidents of robbery in San Francisco reported to the police, while there were 32786 incidents of robbery reported from 2013 to 2022 [(Data source)](https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-2018-to-Present/wg3w-h783). As an overview, the robbery rate has decreased by 8.5% since the decade of 2003 to the last decade, however the number is not significantly decrease, which reflects the robbery is still a key factor that affect the level of crimes in San Francisco.

## Timeseries: How the occurrence of Robbery changed over the time?
<!--  One time-series / bar chart (it's OK to use the "fancy" plot-typs like calendar plots or polar bar-charts from Week 2, Part 4). -->

If we divide the time of the incidents into hourly timeslots, it becomes apparent that the number of robberies reaches its highest point between 2 and 3 pm and remains consistently high until 5 pm. After 5 pm, there is a sharp decline during the evening, but a secondary peak occurs between 1 and 2 am.Between 2 am and 2 pm, the number of incidents increases steadily. 

From a 2003 to 2017, we can see the incidents fluctuated accross years. Specifically, in 2010 and 2011, it has a significant decreased from 2008 and 2009. The [Rand Corporation](https://www.rand.org/) studied this phenomenon on a national level in 2010, concluding that the crime prevention benefit of hiring more officers is well worth the cost. [Reference](https://countyda.sccgov.org/sites/g/files/exjcpb1121/files/10-Year%20Combined%20CA%20Crime%20Stat%20Report.pdf)

However, there was a resurgence in incidents in 2012, with a noticeable gap from the previous year. After analyzing the robbery incidents data in 2012, we observed a marked increase in robberies on the final Sunday in June in San Francisco. Further investigation revealed that this date coincided with the San Francisco LGBT Pride Parade, which started at Beale Street and Market Street and continued down to 8th Street.

<!-- put the plot here -->

## Map: Where does robbery most likely take place?
<!-- One map (use techniques from Week 3 and 4) -->
Let's examine the robbery locations on June 24, 2012, during the Pride Parade in San Francisco which typically occurs on Market Street[(Reference: Wikipedia)](https://en.wikipedia.org/wiki/San_Francisco_Pride#:~:text=The%20San%20Francisco%20Pride%20parade,until%20almost%204%3A00%20pm.).

<!-- put the map here -->
```{python}
import folium
from folium.plugins import HeatMap
df_before_2018 = pd.read_csv('../Police_Department_Incident_Reports__Historical_2003_to_May_2018.csv')
df_before_2018['Date'] = pd.to_datetime(df_before_2018['Date'])
df_before_2018['Year'] = df_before_2018['Date'].dt.year
df_before_2018['Month'] = df_before_2018['Date'].dt.month
df_before_2018['Hour'] = pd.DatetimeIndex(df_before_2018['Time']).hour
df_before_2018 = df_before_2018.loc[df_before_2018['Year'] != 2018]

df_robbery = df_before_2018.loc[df_before_2018['Category']=="ROBBERY"]
df_robbery = df_robbery[df_robbery["Year"] == 2012]
df_robbery_pride = df_robbery[df_robbery['Date'] == '2012-6-24']
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
SF_map
```

The incidence of robbery is relatively high in the vicinity of Market Street, indicating that criminals are more prone to commit robbery in crowded areas, thus increasing their chances of escape. Additionally, the buildings and blocks in the Market Street area are more densely packed, offering additional cover and refuge for criminals. 

This observation also aligns with the result of the heatmap regarding robbery in San Francisco. It reveals the fact that areas with a high concentration of stores and a large population, along with a complex urban infrastructure, are more susceptible to robbery incidents.



**Cluster Correlation idea:** Furthermore, we can select two clusters and a little info box pops up over the cursor printing the correlation between the two clusters.

## Filtering, selecting for group (drunkiness)
<!-- One interactive visualization in Bokeh (Week 6) -->

**First idea for interactive plot:**

Filter based on categories, on selection a little info box with a description tells the user about the category.

**Second idea for interactive plot:**

TODO: investigate some specific event happening in san francisco during the date frame in our dataset(political, shootout, demonstration, party, car chase)

Allow the user to interactive plot different events. And maybe how drunkiness (or some other criminal activity) was related.


# Conclusion