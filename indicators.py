import ta

def add_sma(data):
    data['SMA'] = ta.trend.sma_indicator(data['Close'], window=20)
    return data

def add_ema(data):
    data['EMA'] = ta.trend.ema_indicator(data['Close'], window=20)
    return data

def add_rsi(data):
    data['RSI'] = ta.momentum.rsi(data['Close'], window=14)
    return data

def add_macd(data):
    data['MACD'] = ta.trend.macd(data['Close'])
    data['MACD_Signal'] = ta.trend.macd_signal(data['Close'])
    data['MACD_Hist'] = ta.trend.macd_diff(data['Close'])
    return data

def add_bollinger_bands(data):
    data['BB_High'] = ta.volatility.bollinger_hband(data['Close'], window=20, window_dev=2)
    data['BB_Low'] = ta.volatility.bollinger_lband(data['Close'], window=20, window_dev=2)
    data['BB_Middle'] = ta.volatility.bollinger_mavg(data['Close'], window=20)
    return data
