

import yfinance as yf
import ta
import matplotlib.pyplot as plt

def fetch_data(ticker, start_date, end_date):
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if data.empty:
            raise ValueError(f"No data found for {ticker} in the given date range.")
        return data
    except Exception as e:
        print(f"Failed to download data for {ticker}: {e}")
        return None

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
    elif indicator == 'BB':
        data['BB_High'] = ta.volatility.bollinger_hband(data['Close'], window=20, window_dev=2)
        data['BB_Low'] = ta.volatility.bollinger_lband(data['Close'], window=20, window_dev=2)
        data['BB_Middle'] = ta.volatility.bollinger_mavg(data['Close'], window=20)
    data = data.dropna()
    return data

def plot_data(data, ticker, indicator):
    if data is None or data.empty:
        print("No data to plot.")
        return
        
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
    elif indicator == 'BB':
        plt.plot(data['BB_High'], label='Bollinger High Band')
        plt.plot(data['BB_Low'], label='Bollinger Low Band')
        plt.plot(data['BB_Middle'], label='Bollinger Middle Band')
        plt.fill_between(data.index, data['BB_High'], data['BB_Low'], color='gray', alpha=0.1)
    
    plt.title(f'{ticker} - {indicator}')
    plt.legend()
    plt.show()

def main():
    ticker = input("Enter the asset ticker (e.g., AAPL, MSFT, BTC-USD): ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    indicator = input("Enter the indicator (SMA, EMA, RSI, MACD, BB): ")

    # Fetch data
    data = fetch_data(ticker, start_date, end_date)
    if data is None:
        return
    
    # Add technical indicator
    data = add_technical_indicator(data, indicator)
    
    # Plot data
    plot_data(data, ticker, indicator)

if __name__ == "__main__":
    main()

