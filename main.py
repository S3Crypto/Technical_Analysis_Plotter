import yfinance as yf
import ta
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from data_fetcher import fetch_data

def add_technical_indicators(data, indicators):
    for indicator in indicators:
        if indicator == 'SMA':
            data['SMA'] = ta.trend.sma_indicator(data['Close'], window=20)
        elif indicator == 'EMA':
            data['EMA'] = ta.trend.ema_indicator(data['Close'], window=20)
        elif indicator == 'RSI':
            data['RSI'] = ta.momentum.rsi(data['Close'], window=14)
        elif indicator == 'MACD':
            data['MACD'] = ta.trend.macd(data['Close'])
            data['MACD_Signal'] = ta.trend.macd_signal(data['Close'])
            data['MACD_Hist'] = ta.trend.macd_diff(data['Close'])
        elif indicator == 'BB':
            data['BB_High'] = ta.volatility.bollinger_hband(data['Close'], window=20, window_dev=2)
            data['BB_Low'] = ta.volatility.bollinger_lband(data['Close'], window=20, window_dev=2)
            data['BB_Middle'] = ta.volatility.bollinger_mavg(data['Close'], window=20)
        elif indicator == 'IC':
            data = calculate_ichimoku(data)
    data = data.dropna()
    return data

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

def calculate_fibonacci_levels(data):
    high_price = data['Close'].max()
    low_price = data['Close'].min()
    diff = high_price - low_price

    level1 = high_price - 0.236 * diff
    level2 = high_price - 0.382 * diff
    level3 = high_price - 0.5 * diff
    level4 = high_price - 0.618 * diff
    level5 = high_price - 0.786 * diff

    return [high_price, level1, level2, level3, level4, level5, low_price]

def plot_data(data, ticker, indicators, show_fibonacci=False):
    if data is None or data.empty:
        print("No data to plot.")
        return
    
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Close Price', color='lightblue', linewidth=1.5)
    
    for indicator in indicators:
        if indicator == 'SMA':
            plt.plot(data['SMA'], label='Simple Moving Average', color='orange', linewidth=1.5)
        elif indicator == 'EMA':
            plt.plot(data['EMA'], label='Exponential Moving Average', color='purple', linewidth=1.5)
        elif indicator == 'RSI':
            plt.figure()
            plt.plot(data['RSI'], label='Relative Strength Index', color='green', linewidth=1.5)
            plt.axhline(70, color='r', linestyle='--')
            plt.axhline(30, color='r', linestyle='--')
            plt.legend(fontsize=10)
            plt.title(f'{ticker} - RSI', fontsize=14)
        elif indicator == 'MACD':
            plt.figure()
            plt.plot(data['MACD'], label='MACD', color='blue', linewidth=1.5)
            plt.plot(data['MACD_Signal'], label='Signal Line', color='orange', linewidth=1.5)
            plt.bar(data.index, data['MACD_Hist'], label='MACD Histogram', color='grey', alpha=0.5)
            plt.legend(fontsize=10)
            plt.title(f'{ticker} - MACD', fontsize=14)
        elif indicator == 'BB':
            plt.plot(data['BB_High'], label='Bollinger High Band', color='green', linewidth=1.5)
            plt.plot(data['BB_Low'], label='Bollinger Low Band', color='red', linewidth=1.5)
            plt.plot(data['BB_Middle'], label='Bollinger Middle Band', color='blue', linewidth=1.5)
            plt.fill_between(data.index, data['BB_High'], data['BB_Low'], color='gray', alpha=0.1)
        elif indicator == 'IC':
            plt.plot(data.index, data['Senkou Span A'], label='Senkou Span A', color='green', linewidth=1.5)
            plt.plot(data.index, data['Senkou Span B'], label='Senkou Span B', color='brown', linewidth=1.5)
            plt.fill_between(data.index, data['Senkou Span A'], data['Senkou Span B'], where=np.array(data['Senkou Span A'] >= data['Senkou Span B']), color='green', alpha=0.25)
            plt.fill_between(data.index, data['Senkou Span A'], data['Senkou Span B'], where=np.array(data['Senkou Span A'] < data['Senkou Span B']), color='red', alpha=0.25)
    
    if show_fibonacci:
        fib_levels = calculate_fibonacci_levels(data)
        colors = ['#FF5733', '#FFBD33', '#75FF33', '#33FF57', '#33FFBD', '#3380FF']
        for i, level in enumerate(fib_levels[:-1]):
            plt.fill_between(data.index, fib_levels[i], fib_levels[i+1], color=colors[i], alpha=0.3)
    
    plt.title(f'{ticker} - {", ".join(indicators)}', fontsize=14)
    plt.legend(fontsize=10)
    plt.show()

def main():
    ticker = input("Enter the asset ticker (e.g., AAPL, MSFT, BTC-USD): ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    indicators = input("Enter the indicators (SMA, EMA, RSI, MACD, BB, IC) separated by commas: ").split(',')
    show_fibonacci = input("Show Fibonacci retracement levels? (yes/no): ").lower() == 'yes'

    # Fetch data
    data = fetch_data(ticker, start_date, end_date)
    if data is None:
        return
    
    # Add technical indicators
    data = add_technical_indicators(data, [indicator.strip() for indicator in indicators])
    
    # Plot data
    plot_data(data, ticker, indicators, show_fibonacci)

if __name__ == "__main__":
    main()
