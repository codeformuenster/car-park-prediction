# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:34:02 2017

@author: thor
"""

#%% PACKAGE

from elasticsearch import Elasticsearch
api_link = 'https://elasticsearch.kube.codeformuenster.org/parkleit2/_search'
es = Elasticsearch(api_link, verify_certs=True)
result = es.search()

result
# TODO: get useful data




