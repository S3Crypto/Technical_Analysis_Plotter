import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from fibonacci import calculate_fibonacci_levels

def plot_close(data: pd.DataFrame) -> None:
    """
    Plots the Close price.
    """
    plt.plot(data['Close'], label='Close Price', color='lightblue', linewidth=1.5)

def plot_sma(data: pd.DataFrame) -> None:
    """
    Plots the Simple Moving Average (SMA).
    """
    if 'SMA' in data:
        plt.plot(data['SMA'], label='Simple Moving Average', color='orange', linewidth=1.5)

def plot_ema(data: pd.DataFrame) -> None:
    """
    Plots the Exponential Moving Average (EMA).
    """
    if 'EMA' in data:
        plt.plot(data['EMA'], label='Exponential Moving Average', color='purple', linewidth=1.5)

def plot_rsi(data: pd.DataFrame) -> None:
    """
    Plots the Relative Strength Index (RSI).
    """
    if 'RSI' in data:
        plt.figure()
        plt.plot(data['RSI'], label='Relative Strength Index', color='green', linewidth=1.5)
        plt.axhline(70, color='r', linestyle='--')
        plt.axhline(30, color='r', linestyle='--')
        plt.legend(fontsize=10)
        plt.title('RSI', fontsize=14)

def plot_macd(data: pd.DataFrame) -> None:
    """
    Plots the Moving Average Convergence Divergence (MACD).
    """
    if 'MACD' in data and 'MACD_Signal' in data and 'MACD_Hist' in data:
        plt.figure()
        plt.plot(data['MACD'], label='MACD', color='blue', linewidth=1.5)
        plt.plot(data['MACD_Signal'], label='Signal Line', color='orange', linewidth=1.5)
        plt.bar(data.index, data['MACD_Hist'], label='MACD Histogram', color='grey', alpha=0.5)
        plt.legend(fontsize=10)
        plt.title('MACD', fontsize=14)

def plot_bollinger_bands(data: pd.DataFrame) -> None:
    """
    Plots the Bollinger Bands.
    """
    if 'BB_High' in data and 'BB_Low' in data and 'BB_Middle' in data:
        plt.plot(data['BB_High'], label='Bollinger High Band', color='green', linewidth=1.5)
        plt.plot(data['BB_Low'], label='Bollinger Low Band', color='red', linewidth=1.5)
        plt.plot(data['BB_Middle'], label='Bollinger Middle Band', color='blue', linewidth=1.5)
        plt.fill_between(data.index, data['BB_High'], data['BB_Low'], color='gray', alpha=0.1)

def plot_ichimoku(data: pd.DataFrame) -> None:
    """
    Plots the Ichimoku Cloud indicators.
    """
    if 'Senkou Span A' in data and 'Senkou Span B' in data:
        span_a = data['Senkou Span A'].shift(26)
        span_b = data['Senkou Span B'].shift(26)
        plt.plot(data.index, span_a, label='Senkou Span A', color='green', linewidth=1.5)
        plt.plot(data.index, span_b, label='Senkou Span B', color='brown', linewidth=1.5)
        plt.fill_between(data.index, span_a, span_b, where=(span_a >= span_b), color='green', alpha=0.25)
        plt.fill_between(data.index, span_a, span_b, where=(span_a < span_b), color='red', alpha=0.25)

PLOT_FUNCTIONS = {
    'SMA': plot_sma,
    'EMA': plot_ema,
    'RSI': plot_rsi,
    'MACD': plot_macd,
    'BB': plot_bollinger_bands,
    'IC': plot_ichimoku
}

def plot_data(data: pd.DataFrame, ticker: str, indicators: list, show_fibonacci: bool = False) -> None:
    """
    Plots the data with the specified indicators.
    """
    if data is None or data.empty:
        print("No data to plot.")
        return
    
    plt.figure(figsize=(14, 7))
    plot_close(data)
    
    for indicator in indicators:
        if indicator in PLOT_FUNCTIONS:
            PLOT_FUNCTIONS[indicator](data)
    
    if show_fibonacci:
        fib_levels = calculate_fibonacci_levels(data)
        colors = ['#FF5733', '#FFBD33', '#75FF33', '#33FF57', '#33FFBD', '#3380FF']
        for i, level in enumerate(fib_levels[:-1]):
            plt.fill_between(data.index, fib_levels[i], fib_levels[i+1], color=colors[i], alpha=0.3)
    
    plt.title(f'{ticker} - {", ".join(indicators)}', fontsize=14)
    plt.legend(fontsize=10)
    plt.show()
