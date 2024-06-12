import pytest
import pandas as pd
from indicators import add_sma, add_ema, add_rsi, add_macd, add_bollinger_bands

# Sample DataFrame for testing
data = pd.DataFrame({
    'Close': [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
    'High': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Low': [99, 100, 101, 102, 103, 104, 105, 106, 107, 108]
})

def test_add_sma():
    result = add_sma(data.copy())
    assert 'SMA' in result.columns

def test_add_ema():
    result = add_ema(data.copy())
    assert 'EMA' in result.columns

def test_add_rsi():
    result = add_rsi(data.copy())
    assert 'RSI' in result.columns

def test_add_macd():
    result = add_macd(data.copy())
    assert 'MACD' in result.columns
    assert 'MACD_Signal' in result.columns
    assert 'MACD_Hist' in result.columns

def test_add_bollinger_bands():
    result = add_bollinger_bands(data.copy())
    assert 'BB_High' in result.columns
    assert 'BB_Low' in result.columns
    assert 'BB_Middle' in result.columns
