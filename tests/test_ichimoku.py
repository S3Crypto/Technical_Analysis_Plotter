import pytest
import pandas as pd
from ichimoku import calculate_ichimoku

# Sample DataFrame for testing
data = pd.DataFrame({
    'Close': [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
    'High': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Low': [99, 100, 101, 102, 103, 104, 105, 106, 107, 108]
})

def test_calculate_ichimoku():
    result = calculate_ichimoku(data.copy())
    assert 'Tenkan-sen' in result.columns
    assert 'Kijun-sen' in result.columns
    assert 'Senkou Span A' in result.columns
    assert 'Senkou Span B' in result.columns
    assert 'Chikou Span' in result.columns
