from data_fetcher import fetch_data
from indicators import add_sma, add_ema, add_rsi, add_macd, add_bollinger_bands
from ichimoku import calculate_ichimoku
from plotter import plot_data
import json

with open('config.json') as config_file:
    config = json.load(config_file)

INDICATOR_FUNCTIONS = {
    'SMA': add_sma,
    'EMA': add_ema,
    'RSI': add_rsi,
    'MACD': add_macd,
    'BB': add_bollinger_bands,
    'IC': calculate_ichimoku
}

def main():
    ticker = input("Enter the asset ticker (e.g., AAPL, MSFT, BTC-USD): ")
    start_date = input(f"Enter the start date ({config['date_format']}): ")
    end_date = input(f"Enter the end date ({config['date_format']}): ")
    indicators = input("Enter the indicators (SMA, EMA, RSI, MACD, BB, IC) separated by commas: ").split(',')
    show_fibonacci = input("Show Fibonacci retracement levels? (yes/no): ").lower() == 'yes'

    # Fetch data
    data = fetch_data(ticker, start_date, end_date)
    if data is None:
        return
    
    # Add technical indicators
    for indicator in indicators:
        indicator = indicator.strip()
        if indicator in INDICATOR_FUNCTIONS:
            data = INDICATOR_FUNCTIONS[indicator](data)
    
    # Plot data
    plot_data(data, ticker, [indicator.strip() for indicator in indicators], show_fibonacci)

if __name__ == "__main__":
    main()
