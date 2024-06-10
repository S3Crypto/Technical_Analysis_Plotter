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
