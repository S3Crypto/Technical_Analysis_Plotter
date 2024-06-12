import pytest
import pandas as pd
from plotter import plot_data

# Sample DataFrame for testing
data = pd.DataFrame({
    'Close': [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
    'High': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Low': [99, 100, 101, 102, 103, 104, 105, 106, 107, 108]
})

def test_plot_data():
    from indicators import add_sma, add_ema
    data_with_indicators = add_sma(data.copy())
    data_with_indicators = add_ema(data_with_indicators)
    plot_data(data_with_indicators, 'AAPL', ['SMA', 'EMA'], show_fibonacci=True)
    # Test passes if no exceptions are raised

def test_plot_data_no_indicators():
    plot_data(data, 'AAPL', [], show_fibonacci=False)
    # Test passes if no exceptions are raised

def test_plot_data_ichimoku():
    from ichimoku import calculate_ichimoku
    data_with_ichimoku = calculate_ichimoku(data.copy())
    plot_data(data_with_ichimoku, 'AAPL', ['IC'], show_fibonacci=False)
    # Test passes if no exceptions are raised
