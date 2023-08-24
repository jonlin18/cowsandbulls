#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import sys
import pandas as pd
from pandas.io.json import json_normalize

api_key = ''
  
  

    #create an empty Dict to append the Dataframes to
d = {}

#create a list of cities to iterate over
loc = ['Guilin, China', 'Dissen, Germany','Guatemala City, Guatemala', 'Kandukur, India', 'Nanaimo, British Columbia',
      'Uijeongbu-si, South Korea', 'Yangon, Myanmar', 'Jalpa de Mendez, Mexico', 'Enugu, Nigeria', 
      'Peterhead, Scotland', 'Lima, Peru', 'Singapore, Singapore', 'Kaohsiung, Taiwan', 'Grimesland, North Carolina',
      'Visalia, California', 'Colonia del Sacramento, Uruguay']


#make a for loop to iterate over the cities
for city in loc:
#  Geolocate Peterhead, Scotland to get it's latitude and longitude
  
    URL = 'http://api.openweathermap.org/geo/1.0/direct'
    geo = f'{URL}?q={city}&limit=5&appid={api_key}'
    resp = requests.get( geo )

    if resp.status_code != 200:  # Failure?
          print( f'Error geocoding {city}: {resp.status_code}' )
          sys.exit( 1 )
  
  #  OpenWeatherMap returns a list of matching cities, up to the limit specified
  #  in the API call; even if you only ask for one city (limit=5), it's still
  #  returned as a 1-element list
    if len( resp.json() ) == 0:  # No such city?
        print( f'Error locating city {city}; {resp.status_code}' )
        sys.exit( 2 )
    a = resp.json()

    if type( a) == list:  # List of cities?
        lat = a[ 0 ][ 'lat' ]
        lon = a[ 0 ][ 'lon' ]

    else:  # Unknown city?
        print( f'Error, invalid data returned for city {city}, {resp.status_code}' )
        sys.exit( 3 )
  
  #  Use Peterhead's latitude and longitude to get it's 5-day forecast in 3-hour
  #  blocks, also change the units from Kelvin to Celsius

    URL = 'http://api.openweathermap.org/data/2.5/forecast'
    forecast = f'{URL}?lat={lat}&lon={lon}&units=metric&appid={api_key}'
    resp = requests.get( forecast )

    if resp.status_code != 200:  # Failure?
        print( f'Error retrieving data: {resp.status_code}' )
        sys.exit( 4 )

    data = resp.json()

#flatten nested JSONs into a DataFrame
    d[city] = pd.json_normalize(data['list'], sep = '_')





# In[2]:


def tmin(df):
    """returns the min temp of that day"""
    return df['main_temp_min'].min()

def tmax(df):
    """returns the max temp of that day"""
    return df['main_temp_max'].max()


# In[3]:


#empty list to append data to
Min_1 = []
Max_1 = []
Min_2 = []
Max_2 = []
Min_3 = []
Max_3 = []
Min_4 = []
Max_4 = []
Min_Avg = []
Max_Avg = []

#has to be in for loop
for city in loc:
    c = d[city]
#set up 'tomorrow'
    tmw = []
    for index, value in enumerate(c['dt_txt']):

        if '00:00:00' in value:
            tmw.append(index)

#Create the 4 days of subsection
#day 1, min max
    day1 = c.iloc[tmw[0]:tmw[1]]
    day1min = tmin(day1)
    day1max = tmax(day1)
    Min_1.append(day1min)
    Max_1.append(day1max)

#day 2, min max
    day2 = c.iloc[tmw[1]:tmw[2]]
    day2min = tmin(day2)
    day2max = tmax(day2)
    Min_2.append(day2min)
    Max_2.append(day2max)

#day3, min max
    day3 = c.iloc[tmw[2]:tmw[3]]
    day3min = tmin(day3)
    day3max = tmax(day3)
    Min_3.append(day3min)
    Max_3.append(day3max)
#day4, min max
    day4 = c.iloc[tmw[3]:tmw[4]]
    day4min = tmin(day4)
    day4max = tmax(day4)
    Min_4.append(day4min)
    Max_4.append(day4max)
    
#add to min avg and max avg column
    min_avg = round(((day1min + day2min + day3min + day4min)/4), 2)
    max_avg = round(((day1max + day2max + day3max + day4max)/4), 2)
    Min_Avg.append(min_avg)
    Max_Avg.append(max_avg)
    
    


# In[4]:


#combine the lists into a dataframe
#zip merges all the items per index position of these lists together into one tuple. then all these tuples are turned into a list of tuples
#each tuple is one row in the df
#set the index equal to the cities
final_df = pd.DataFrame(list(zip(Min_1, Max_1, Min_2, Max_2, Min_3, Max_3, Min_4, Max_4, Min_Avg, Max_Avg)),
                        index = loc, 
              columns=['Min 1', 'Max 1', 'Min 2', 'Max 2', 'Min 3', 'Max 3', 'Min 4', 'Max 4', 'Min Avg', 'Max Avg'])
#add a name for the index

final_df.index.name = "City"


print(final_df)




# In[ ]:




