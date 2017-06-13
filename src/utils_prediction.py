"""
Utils for predicting free capacities.

Created on Mon May 29 07:06:24 2017
@author: Thorben Jensen
"""

import get_data
import datetime
from sklearn.ensemble import RandomForestRegressor


def forecast_linear(dt, car_park):
    """Simple linear prediction."""
    # get latest two observations, before the given point in time
    df = get_data.get_all_data()
    df2 = df[(df.datetime < str(dt)) &
             (df.name == car_park)]
    df3 = df2.sort_values(by='datetime')
    df4 = df3.tail(n=2)
    second_latest = df4.head(n=1)
    latest = df4.tail(n=1)

    # calculate delta for capacity (per second)
    diff_time = (latest.datetime.iloc[0] - second_latest.datetime.iloc[0])
    diff_sec = diff_time.seconds
    diff_cap = (latest.cap.iloc[0] - second_latest.cap.iloc[0])
    d_cap_per_sec = diff_cap / diff_sec

    # linearly extrapolate to the requested point in time
    fcst_sec = (dt - latest.datetime.iloc[0]).seconds
    fcst_cap = latest.cap.iloc[0] + d_cap_per_sec * fcst_sec

    # limit prediction to min-max range of all observations for this car-park
    fcst_cap = max(fcst_cap, 0)
    return(fcst_cap)
    
    
def forecast_regression(dt, car_park):
    """Regression-based forecast of time series"""
    # get training data (for 'car_park')
    # TODO
    # train random forest model
    rf = RandomForestRegressor()
    # TODO
    # make prediction for 'dt'
    # TODO
    # return prediction
    # TODO
    

if __name__ == '__main__':
    '''Set random point in time and a car park.'''
    dt = datetime.datetime(2017, 1, 2, 19)
    car_park = 'PH Bremer Platz'

    fcst_cap = forecast_linear(dt, car_park)
    print("Forecasted free capacity: %i" % fcst_cap)
