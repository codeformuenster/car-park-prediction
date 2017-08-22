u"""
Crawl wunderground.com for historic weather data for Münster.

Created on Tue Jun 20 20:59:56 2017
@author: thor
"""

import requests
import re
from datetime import date
import dateutil.parser as dp
import time


def get_mean_temperature(day):
    """Crawl the weather."""
    url = 'https://www.wunderground.com/history/airport/EDDG/' \
        + str(day.year) + '/' + str(day.month) + '/' + str(day.day) \
        + '/DailyHistory.html?req_city=M%C3%BCnster'
    html = requests.get(url).text
    pattern = 'Mean Temperature.*?<span class="wx-value">([\w\.-]+)'
    mean_temperature = float(re.search(pattern, html, re.S).group(1))
    return mean_temperature


def dates_without_mean_temperature(df):
    """Get dates that are missing the field 'mean_temperature'."""
    return df.loc[df['mean_temperature'].isnull()].date.unique()


def crawl_and_set_mean_temperature(df, isodate):
    """Crawl mean temperature for a date and add to dataframe."""
    day = dp.parse(isodate).date()
    mean_temp = get_mean_temperature(day)
    df.loc[df['date'] == isodate, 'mean_temperature'] = mean_temp


def set_all_missing_mean_temperatures(df):
    """Iterate over relevant dates and add all missing mean termperatures."""
    dates_without_mean_temp = dates_without_mean_temperature(df)
    for date_without_mean_temp in dates_without_mean_temp:
        print('Adding mean_temperature for date %s' % date_without_mean_temp)
        crawl_and_set_mean_temperature(df, date_without_mean_temp)
        time.sleep(3)


if __name__ == "__main__":

    day = date(2017, 1, 23)
    mean_temperature = get_mean_temperature(day)
    print('Mean temperature in Münster on %s: %f'
          % (day.isoformat(), mean_temperature))
