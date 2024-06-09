# Technical Analysis Tool

This project is a technical analysis tool that fetches historical data for a given asset, applies various technical indicators, and visualizes the results. The tool supports multiple indicators such as Simple Moving Average (SMA), Exponential Moving Average (EMA), Relative Strength Index (RSI), and Moving Average Convergence Divergence (MACD).

## Features

- Fetch historical price data for various assets.
- Calculate and plot different technical indicators.
- Visualize the data with matplotlib.

## Requirements

- Python 3.x
- `pandas`
- `numpy`
- `matplotlib`
- `yfinance`
- `ta`

Here's an example of how to use the tool:

Enter the asset ticker (e.g., AAPL, MSFT, BTC-USD): AAPL
Enter the start date (YYYY-MM-DD): 2020-01-01
Enter the end date (YYYY-MM-DD): 2023-01-01
Enter the indicator (SMA, EMA, RSI, MACD): SMA
The tool will then fetch the historical data for Apple Inc. (AAPL) from January 1, 2020, to January 1, 2023, calculate the Simple Moving Average (SMA), and display a plot of the closing prices along with the SMA.

Contributing
Contributions are welcome! If you have suggestions for improvements or additional features, please create an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
yfinance for fetching historical market data.
ta for providing technical analysis indicators.
