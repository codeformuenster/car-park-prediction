# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:34:02 2017

@author: thor
"""

import json
import pandas as pd

from urllib.request import urlopen


#%% package elasticsearch
# TODO: test scrolling

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

api_link = 'https://elasticsearch.kube.codeformuenster.org/parkleit2/_search'
es = Elasticsearch(api_link, 
                   verify_certs=True)

s = Search(using=es)
s = s.query("match_all", fields=[])
s.execute()

#s.fields([])
#ids = [h.meta.id for h in s.scan()]

#es.search()
#
#result


#%% get json

size = 10000
api_link = \
    'https://elasticsearch.kube.codeformuenster.org/parkleit2/_search?size=' + str(size)
response = urlopen(api_link)
result = response.read().decode('utf-8')

#%% Extract hits from json

parsed = json.loads(result)
#print(json.dumps(parsed, indent=2, sort_keys=False))
hits = parsed['hits']['hits']
observations = [ x['_source'] for x in hits ]
print('Retrieved %s hits form API.' % len(hits))

#%% hits to Dataframe, extract (name, timestamp, free)

data_all = pd.DataFrame(observations)
data_select = data_all[['name', 'timestamp', 'free']]
df = data_select.dropna(axis=0, how='any')

#%% inspect individual timeline

df2 = df.loc[df['name'] == 'PH Aegidii']
df2 = df2.sort(columns='timestamp')
