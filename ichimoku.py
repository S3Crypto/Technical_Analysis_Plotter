import pandas as pd

def calculate_ichimoku(data):
    high_9 = data['High'].rolling(window=9).max()
    low_9 = data['Low'].rolling(window=9).min()
    data['Tenkan-sen'] = (high_9 + low_9) / 2

    high_26 = data['High'].rolling(window=26).max()
    low_26 = data['Low'].rolling(window=26).min()
    data['Kijun-sen'] = (high_26 + low_26) / 2

    data['Senkou Span A'] = ((data['Tenkan-sen'] + data['Kijun-sen']) / 2).shift(26)

    high_52 = data['High'].rolling(window=52).max()
    low_52 = data['Low'].rolling(window=52).min()
    data['Senkou Span B'] = ((high_52 + low_52) / 2).shift(26)

    data['Chikou Span'] = data['Close'].shift(-26)

    return data
