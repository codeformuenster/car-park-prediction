"""
Crawl wunderground.com for historic weather data for Münster.
Created on Tue Jun 20 20:59:56 2017
@author: thor
"""

import requests
import re
from datetime import date

def crawl_weather(day):
    url = 'https://www.wunderground.com/history/airport/EDDG/'+str(day.year)+'/'+str(day.month)+'/'+str(day.day)+'/DailyHistory.html?req_city=M%C3%BCnster'
    html = requests.get(url).text
    pattern = 'Mean Temperature.*?<span class="wx-value">([\w\.-]+)'
    mean_temperature = float(re.search(pattern, html, re.S).group(1))
    return mean_temperature

if __name__ == "__main__":
    day = date(2017,1,23)
    mean_temperature = crawl_weather(day)
    print('Mean temperature in Münster on %s: %f' \
          % (day.isoformat(), mean_temperature) )
