

import yfinance as yf
import ta
import matplotlib.pyplot as plt

def fetch_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

def add_technical_indicator(data, indicator):
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
    return data

def plot_data(data, ticker, indicator):
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Close Price')
    
    if indicator == 'SMA':
        plt.plot(data['SMA'], label='Simple Moving Average')
    elif indicator == 'EMA':
        plt.plot(data['EMA'], label='Exponential Moving Average')
    elif indicator == 'RSI':
        plt.plot(data['RSI'], label='Relative Strength Index')
        plt.axhline(70, color='r', linestyle='--')
        plt.axhline(30, color='r', linestyle='--')
    elif indicator == 'MACD':
        plt.plot(data['MACD'], label='MACD')
        plt.plot(data['MACD_Signal'], label='Signal Line')
        plt.bar(data.index, data['MACD_Hist'], label='MACD Histogram', color='grey', alpha=0.5)
    
    plt.title(f'{ticker} - {indicator}')
    plt.legend()
    plt.show()

def main():
    ticker = input("Enter the asset ticker (e.g., AAPL, MSFT, BTC-USD): ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    indicator = input("Enter the indicator (SMA, EMA, RSI, MACD): ")

    # Fetch data
    data = fetch_data(ticker, start_date, end_date)
    
    # Add technical indicator
    data = add_technical_indicator(data, indicator)
    
    # Plot data
    plot_data(data, ticker, indicator)

if __name__ == "__main__":
    main()

