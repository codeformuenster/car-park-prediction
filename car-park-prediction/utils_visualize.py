# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 21:21:23 2017

@author: thor
"""

import get_data
from ggplot import aes, geom_line, facet_wrap, ggplot


df = get_data.get_all_data()

p = ggplot(df, aes('datetime', 'cap', group='date')) + \
    geom_line(alpha=0.2) + \
    facet_wrap('name')
p.save('../output/time_series.pdf')
p