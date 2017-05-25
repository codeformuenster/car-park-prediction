# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:34:02 2017

@author: thor
"""

import sqlite3
import pandas as pd

#%% get DataFrame from SQLite

con = sqlite3.connect("../database/parkleit2.sqlite")
df = pd.read_sql(sql="SELECT * FROM parkleit2", con=con)
con.close()

#%% TODO: visualize time series

df