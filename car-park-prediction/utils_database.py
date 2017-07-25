"""
Get observations from local SQLite database.

Created on Tue May 23 21:34:02 2017
@author: Thorben Jensen
"""

import sqlite3
import pandas as pd


# %% database to pandas, generate features

def get_all_data():
    """Get all observations from database."""
    con = sqlite3.connect("../database/parkleit2.sqlite")
    df = pd.read_sql(sql="SELECT * FROM parkleit2", con=con)
    con.close()
    return df


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
