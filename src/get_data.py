# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:34:02 2017

@author: thor
"""

#%% PACKAGE elasticsearch

#from elasticsearch import Elasticsearch
#api_link = 'https://elasticsearch.kube.codeformuenster.org/parkleit2/_search'
#es = Elasticsearch(api_link, 
#                   verify_certs=True,
#                   maxsize=100)
#result = es.search()
#
#result

#%% get json

from urllib.request import urlopen

api_link = 'https://elasticsearch.kube.codeformuenster.org/parkleit2/_search?size=1000'
response = urlopen(api_link)
result = response.read().decode('utf-8')

#%% Extract hits from json

import json

parsed = json.loads(result)
#print(json.dumps(parsed, indent=2, sort_keys=False))
hits = parsed['hits']['hits']
print('Retrieved %s hits form API.' % len(hits))

#%% hits to Dataframe

import pandas as pd

df = pd.DataFrame(hits)
df

# TODO: make this a table

