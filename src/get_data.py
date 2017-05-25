# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:34:02 2017

@author: thor
"""

import sqlite3
import pandas as pd
from ggplot import *

#%% database to pandas

con = sqlite3.connect("../database/parkleit2.sqlite")
df = pd.read_sql(sql="SELECT * FROM parkleit2", con=con)
con.close()

#%% generate features

df['datetime'] = pd.to_datetime(df.timestamp)
df['cap'] = pd.to_numeric(df.free)
df['time'] = df.datetime.dt.time  # time of the day
df['date'] = df.datetime.dt.date  # date

#%% visualize time series

ggplot(df, aes('time', 'cap', group='date')) + \
    geom_line(alpha=0.2) + \
    facet_wrap('name')
