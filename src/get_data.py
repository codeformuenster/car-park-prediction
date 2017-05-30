# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:34:02 2017

@author: Thorben Jensen
"""

import sqlite3
import pandas as pd
from ggplot import *

#%% database to pandas, generate features

def get_data():
    con = sqlite3.connect("../database/parkleit2.sqlite")
    df = pd.read_sql(sql="SELECT * FROM parkleit2", con=con)
    con.close()
    df['datetime'] = pd.to_datetime(df.timestamp)
    df['cap'] = pd.to_numeric(df.free)
    df['time'] = df.datetime.dt.time  # time of the day
    df['date'] = df.datetime.dt.date  # date
    return df

#%% visualize all data
if __name__ == '__main__':    
    df = get_data()

    p = ggplot(df, aes('time', 'cap', group='date')) + \
        geom_line(alpha=0.2) + \
        facet_wrap('name')   
    p.save('../output/time_series.pdf')
    p