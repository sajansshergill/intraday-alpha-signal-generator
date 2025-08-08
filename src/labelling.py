def add_momentum_signal(df, period=15, buy_thresh=1.0, sell_thresh=-1.0):
    df['momentum'] = df['close'].pct_change(periods=period)
    df['momentum_signal'] = (df['momentum'] - df['momentum'].mean()) / df['momentum'].std()

    df['signal'] = 0
    df.loc[df['momentum_signal'] > buy_thresh, 'signal'] = 1
    df.loc[df['momentum_signal'] < sell_thresh, 'signal'] = -1
    return df
