# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:34:02 2017

@author: Thorben Jensen
"""

import sqlite3
import pandas as pd
from ggplot import *

#%% database to pandas, generate features

def get_all_data():
    con = sqlite3.connect("../database/parkleit2.sqlite")
    df = pd.read_sql(sql="SELECT * FROM parkleit2", con=con)
    con.close()
    df['cap'] = pd.to_numeric(df.free)
    df['time'] = df.datetime.dt.time  # time of the day
    df['date'] = df.datetime.dt.date  # date
    return df

def get_latest_n():
    '''Get latest N observations, previous to given timestamp.'''
    '''
    TODO: quick query. something like...
    
    SELECT 
        	name, datetime, free
    FROM parkleit2
    WHERE 
        	name = 'PH Bremer Platz'
         AND datetime < '2017-01-02 19:00:00'
    ORDER BY datetime DESC
    LIMIT 2
    '''
    pass

def set_indices():
    '''Sets indices to database, for quicker queries.'''
    pass    
    # TODO

#%% visualize all data
if __name__ == '__main__':   
    df = get_all_data()

    p = ggplot(df, aes('time', 'cap', group='date')) + \
        geom_line(alpha=0.2) + \
        facet_wrap('name')   
    p.save('../output/time_series.pdf')
    p