
# coding: utf-8

# # Assignment 2
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# An NOAA dataset has been stored in the file `data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv`. The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) [Daily Global Historical Climatology Network](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt) (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
# 
# Each row in the assignment datafile corresponds to a single observation.
# 
# The following variables are provided to you:
# 
# * **id** : station identification code
# * **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# * **element** : indicator of element type
#     * TMAX : Maximum temperature (tenths of degrees C)
#     * TMIN : Minimum temperature (tenths of degrees C)
# * **value** : data value for element (tenths of degrees C)
# 
# For this assignment, you must:
# 
# 1. Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
# 2. Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
# 3. Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
# 4. Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
# 
# The data you have been given is near **Ann Arbor, Michigan, United States**, and the stations the data comes from are shown on the map below.

# In[ ]:

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(400,'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89')
#leaflet_plot_stations(100,'015fffba7a19bad88ca6cbed7ba551f65e4762769effa014ee201512')


# In[2]:

import matplotlib.pyplot as plt
import pandas as pd
df1 = pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
df1.sort('Date')


# In[ ]:




# In[3]:

df1['Year'], df1['Month-Date'] = zip(*df1['Date'].apply(lambda x: (x[:4], x[5:])))
df1


# In[4]:

df1 = df1[df1['Month-Date'] != '02-29']
len(df1)


# In[6]:

import numpy as np
temp_min = df1[(df1['Element'] == 'TMIN') & (df1['Year'] != '2015')].groupby('Month-Date').aggregate({'Data_Value':np.min})
temp_max = df1[(df1['Element'] == 'TMAX') & (df1['Year'] != '2015')].groupby('Month-Date').aggregate({'Data_Value':np.max})
temp_max


# In[7]:

import numpy as np
temp15_min = df1[(df1['Element'] == 'TMIN') & (df1['Year'] == '2015')].groupby('Month-Date').aggregate({'Data_Value':np.min})
temp15_max = df1[(df1['Element'] == 'TMAX') & (df1['Year'] == '2015')].groupby('Month-Date').aggregate({'Data_Value':np.max})
#temp15_min.tail(100)
temp15_max


# In[8]:

broken_min = temp15_min[temp15_min['Data_Value'] < temp_min['Data_Value']]
broken_min = broken_min[broken_min['Data_Value'].isnull() == False]
broken_min


# In[10]:

broken_max = temp15_max[temp15_max['Data_Value'] > temp_max['Data_Value']]
broken_max = broken_max[broken_max['Data_Value'].isnull() == False]
broken_max



# In[11]:

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime as dt


plt.figure()
# plot low temp and high temp data
xdate = np.array(temp_min.index)
x = [dt.datetime.strptime(d, '%m-%d') for d in xdate]
xaxis = mdates.date2num(x)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.gcf().autofmt_xdate()
# Create a line graph of the record high and record low temperatures by day of the year over the period 2005-2014
plt.plot(xaxis, temp_min.values, 'g', label = 'record low')
plt.plot(xaxis, temp_max.values, 'm', label = 'record high')

#The area between the record high and record low temperatures for each day is shaded.
# fill_between() requires a datetime format for x coordinate
plt.gca().fill_between(x, temp_min['Data_Value'], temp_max['Data_Value'], facecolor = 'yellow', alpha = 0.25)

# Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
xdate1 = np.array(broken_min.index)
x1 = [dt.datetime.strptime(d, '%m-%d') for d in xdate1]
xaxis1 = mdates.date2num(x1)
plt.scatter(xaxis1, broken_min, s = 10, c = 'b', label = 'broken low')

xdate2 = np.array(broken_max.index)
x2 = [dt.datetime.strptime(d, '%m-%d') for d in xdate2]
xaxis2 = mdates.date2num(x2)
plt.scatter(xaxis2, broken_max, s = 10, c = 'r', label = 'broken high')

plt.xlabel('Day of the Year')
plt.ylabel('Temperature (Tenths of Degrees C)')
plt.title('Temperature Summary Plot near Michigan')
plt.legend(loc = 4, frameon = False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.show()


# In[ ]:



