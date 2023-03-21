---
title: Storyline
subtitle: Second assignment socviz
---

Let's create a nice story

# Introduction

- TODO Explaining the dataset
- TODO abstract for the story
- TODO basic summary statistics/info for the dataset


## Timeseries : Progression of drunkiness 
<!--  One time-series / bar chart (it's OK to use the "fancy" plot-typs like calendar plots or polar bar-charts from Week 2, Part 4). -->
> [reference]: https://data.sfgov.org/browse?category=Public+Safety  Dataset

First we investigate how drunkiness changes over time, especially into the period during COVID.
![Calendar plot](https://i.imgur.com/aN7iyQs.png)

Let's look into a few weeks
![Drunkness - weekdays](https://i.imgur.com/1JKFHTL.png)


![Drunkness - hourly](https://i.imgur.com/S8o4guz.png)

## Comparing areas of criminal activity
<!-- One map (use techniques from Week 3 and 4) -->

Here we have an interactive map of San Francisco, allowing us to zoom into a more specific area and investigate drunkineess and other criminal activity between different streets.  
![Map of SF](https://i.imgur.com/6Zctfgi.png)

![Zoom in heatmaps of 2 clusters](https://i.imgur.com/9oy7O53.png)

compare 2 streets (Market Street vs. Catro Street) with strong density of occurences of drunkness, and see what is going on

For now assume we do one map includes 2 streets and the clusters of incidents. And attempt to present them by zooming in the streets seperately

**Cluster Correlation idea:** Furthermore, we can select two clusters and a little info box pops up over the cursor printing the correlation between the two clusters.

## Filtering, selecting for group (drunkiness)
<!-- One interactive visualization in Bokeh (Week 6) -->

**First idea for interactive plot:**

Filter based on categories, on selection a little info box with a description tells the user about the category.

**Second idea for interactive plot:**

TODO: investigate some specific event happening in san francisco during the date frame in our dataset(political, shootout, demonstration, party, car chase)

Allow the user to interactive plot different events. And maybe how drunkiness (or some other criminal activity) was related.


__Questions__
- Are we limited to the dataset/timeframe? (Is it possible to look into the data after 2020 during covid?)
- Can we include multiple datasets? (as supplementery)
- 

<!-- [caption](./assets/image.png){width=70%} -->