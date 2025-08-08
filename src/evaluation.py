import numpy as np


def backtest_strategy(df):
    df['strategy_return'] = df['log_return'] * df['signal'].shift(1)
    df['cumulative_strategy'] = df['strategy_return'].cumsum()
    df['cumulative_market'] = df['log_return'].cumsum()
    return df

def compute_metrics(df):
    sharpe_ratio = df['strategy_return'].mean() / df['strategy_return'].std() * np.sqrt(252 * 24 * 60)  # per minute Sharpe
    accuracy = (df['signal'].shift(1) * df['log_return'] > 0).mean()
    return {'sharpe_ratio': sharpe_ratio, 'accuracy': accuracy}
