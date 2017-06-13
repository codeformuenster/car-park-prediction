"""
Get observations from local SQLite database.

Created on Tue May 23 21:34:02 2017
@author: Thorben Jensen
"""

import sqlite3
import pandas as pd
from ggplot import aes, geom_line, facet_wrap, ggplot

# %% database to pandas, generate features

def get_all_data():
    """Get all observations from database."""
    con = sqlite3.connect("../database/parkleit2.sqlite")
    df = pd.read_sql(sql="SELECT * FROM parkleit2", con=con)
    con.close()
    return df


def engineer_features():
    """Feature engineering for regression."""
    # get data 
    df = get_all_data()

    # engineer simple features
    df['datetime'] = pd.to_datetime(df.timestamp)  # TODO: can be removed?
    df['cap'] = pd.to_numeric(df.free)
    df['time'] = df.datetime.dt.time  # time of the day
    df['date'] = df.datetime.dt.date  # date
    df['year'] = df.datetime.dt.year  # year
    df['month'] = df.datetime.dt.month  # month number
    df['weekday'] = df.datetime.dt.weekday  # weekday number
    df['weekend'] = (df.datetime.dt.weekday > 5).astype(int)  # weekend flag
    df['hour'] = df.datetime.dt.hour  # hour
    df['minute'] = df.datetime.dt.minute  # minute
    df['second'] = df.datetime.dt.second  # minute

    # lag reatures
    # TODO # 30 minutes ago (interpolated)

    # engineer external features
    # TODO # 'bank holiday North-Rhine Westfalia'
    # TODO # 'bank holiday Niedersachsen'
    # TODO # 'bank holiday Netherlands'
    # TODO # avg. temperature of day
    # TODO # rain probability of day
    # TODO # X coordinate car park
    # TODO # Y coordinate car park
    # TODO # Send
    # TODO # Events from event API?
    # TODO # football match?
    
    # update database
    con = sqlite3.connect("../database/parkleit2.sqlite")
    df.to_sql(name="parkleit2", con=con, if_exists="replace", index=False)
    con.close()



def get_latest_n():
    """Get latest N observations, previous to given timestamp."""
    '''
    TODO: quick query for prediction. something like...

    SELECT name, datetime, free
    FROM parkleit2
    WHERE name = 'PH Bremer Platz'
         AND datetime < '2017-01-02 19:00:00'
    ORDER BY datetime DESC
    LIMIT 2
    '''
    pass


def set_indices():
    """Set indices to database, for quicker queries."""
    pass
    # TODO
