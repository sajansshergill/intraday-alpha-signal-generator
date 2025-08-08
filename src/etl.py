
import pandas as pd

def load_binance_csv(path):
    df = pd.read_csv(path, header=None)
    df.columns = [
        'timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time',
        'quote_asset_volume', 'num_trades', 'taker_buy_base_volume',
        'taker_buy_quote_volume', 'ignore'
    ]
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms', errors='coerce')
    df = df.dropna(subset=['timestamp'])
    df.set_index('timestamp', inplace=True)
    df = df.astype(float, errors='ignore')
    return df
