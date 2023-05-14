## Alejandra

climate = pd.read_csv('https://raw.githubusercontent.com/zuzell/socialdata/main/Data/climate_CPH.csv')
 
# Modify date format
climate['Dato']=pd.to_datetime(climate['date_mine'], format='%Y.%m.%d')

# Select from 2005 to 2014
climate = climate[climate['Year'] >= 2005]
climate = climate[climate['Year'] <= 2014]

# create dataframe
gg = df_alldays.groupby(['Dato']).sum()

## Merge both
climate['Count'] = list(gg['Count'])

## Plot
sns.set_style('darkgrid')
sns.set(font_scale=1.5)

y = climate['Count']
x = climate['AvgTemperature']
xticks = [str(i)[:10] for i in climate['Dato']]
xticks = climate['Year']

y = (y - np.mean(y))/np.std(y)
x = (x - np.mean(x))/np.std(x)
N = len(y)

f, ax = plt.subplots(figsize=(15, 5))
plt.plot(range(N), x, '-', color='#3e059b', label='AvgTemperature', alpha=0.8)
plt.plot(range(N), y, color='#f3894a', label='Bike counts', alpha=0.8)
# Set the x-tick values
plt.xticks(range(0,N,365), xticks[0:N:365], rotation=45)
plt.legend()