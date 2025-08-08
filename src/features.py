import numpy as np
import pandas as pd

def compute_log_return(df):
    df['log_return'] = np.log(df['close'] / df['close'].shift(1))
    return df

def compute_rolling_volatility(df, window=15):
    df['rolling_volatility'] = df['log_return'].rolling(window=window).std()
    return df

def extract_time_features(df):
    df['hour'] = df.index.hour
    df['weekday'] = df.index.weekday
    return df

def add_all_features(df):
    df = compute_log_return(df)
    df = compute_rolling_volatility(df)
    df = extract_time_features(df)
    return df
