import pandas as pd
df_before_2018 = pd.read_csv('data/Police_Department_Incident_Reports__Historical_2003_to_May_2018.csv')
df_before_2018['Date'] = pd.to_datetime(df_before_2018['Date'])
df_before_2018['Year'] = df_before_2018['Date'].dt.year
df_before_2018['Month'] = df_before_2018['Date'].dt.month
df_before_2018['Hour'] = pd.DatetimeIndex(df_before_2018['Time']).hour
df_before_2018 = df_before_2018.loc[df_before_2018['Year'] != 2018]
df_robbery = df_before_2018.loc[df_before_2018['Category']=="ROBBERY"]
df_robbery = df_robbery[df_robbery["Year"] == 2012]
df_robbery_pride = df_robbery[df_robbery['Date'] == '2012-6-24']
get_XY = list(zip(list(df_robbery_pride["Y"]), list(df_robbery_pride["X"])))
dir(df_before_2018)
df_before_2018.to_csv('data/before_2018.csv')