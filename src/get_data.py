# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:34:02 2017

@author: thor
"""

import urllib.request
import pandas as pd

#%%

api_link = 'https://elasticsearch.kube.codeformuenster.org/parkleit2/_search'
result = urllib.request.urlopen(api_link).read()
pd.read_json(result)


#%% TODO: get time series



