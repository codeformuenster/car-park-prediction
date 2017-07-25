"""Engineer features."""

from utils_database import get_all_data
import pandas as pd
import sqlite3


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

    # lag reatures
    # TODO # 30 minutes ago (interpolated)  # TODO: speed up interpolation

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
