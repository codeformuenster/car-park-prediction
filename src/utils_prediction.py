# -*- coding: utf-8 -*-
"""
Created on Mon May 29 07:06:24 2017

@author: Thorben Jensen
"""

import pandas as pd
import get_data
import datetime

#%% get data

df = get_data.get_data()

#%% simple linear prediction

# set random point in time and a car park
dt = datetime.datetime(2017, 4, 2, 19)
car_park = 'PH Bremer Platz'

# get latest two observations (before the given point in time)
df2 = df[(df.datetime < str(dt)) &
         (df.name == car_park)]
df2.sort_values(by='datetime')
        

# ]: df2.tail(n=2)??
# linearly extrapolate to the point in time
# TODO

# limit prediction to min-max range of all observations for car-park
# TODO

