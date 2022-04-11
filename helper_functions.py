import datetime as dt
import pandas as pd

def epochTime(df):
    """ Converts epochTime to datetime format YYYY-MM-DD """
    
    df.drop(columns = ['Unnamed: 0'],inplace=True)
    df['Time'] = df['Time'] / 1000 - 1000
    df['Time'] = pd.to_datetime(df['Time'], unit='s').apply(lambda x: x.strftime('%Y-%m-%d'))
    df.set_index('Time', inplace=True)
    return df
