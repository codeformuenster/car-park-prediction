"""
Get all observations from elasticsearch and add to local SQlite db.

Created on Thu May 25 11:28:15 2017
@author: thor
# TODO: move this to utils_database.py
"""

from elasticsearch import Elasticsearch
import pandas as pd
import sqlite3

# %% SETUP ELASTICSEARCH

api_link = 'https://elasticsearch.kube.codeformuenster.org'
es = Elasticsearch(api_link, verify_certs=True)

# %% PAGE TO PANDAS


def page_to_df(page):
    """Convert search page to pandas DataFrame."""
    hits = page['hits']['hits']
    observations = [x['_source'] for x in hits]
    data_all = pd.DataFrame(observations)
    data_select = data_all[['name', 'timestamp', 'free']]
    df = data_select.dropna(axis=0, how='any')
    return df

# %% SCROLL
page = es.search(
    index='parkleit2',
    scroll='10m',
    size=10000,
    body={"query": {"match_all": {}}}
)

sid = page['_scroll_id']
scroll_size = page['hits']['total']

# store hits locally
df_all = page_to_df(page)

# report on progress
total_size = scroll_size
print('Total scroll size: %s' % total_size)
retrieved = 0

while (scroll_size > 0):
    print("Scrolling...")

    page = es.scroll(scroll_id=sid, scroll='10m')
    sid = page['_scroll_id']  # Update the scroll ID

    # store hits locally
    if len(page['hits']['hits']) > 0:
        df_new = page_to_df(page)
        df_all = pd.concat([df_all, df_new])
        print('Items stored in "df_all": %i' % len(df_all.index))

    # report on progress
    scroll_size = len(page['hits']['hits'])
    print("scroll size: %i" % scroll_size)
    retrieved += scroll_size
    print('Retrieved %i of %i' % (retrieved, total_size))

# %% generate 'datetime' feature and store in local db

df_all['datetime'] = pd.to_datetime(df_all.timestamp)

con = sqlite3.connect("../database/parkleit2.sqlite")
df_all.to_sql(name="parkleit2", con=con, if_exists="replace")
con.close()
