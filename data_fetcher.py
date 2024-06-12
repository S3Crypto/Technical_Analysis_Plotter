import logging
import yfinance as yf
import pandas as pd

def fetch_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Fetches historical data for a given ticker symbol.

    Parameters:
    ticker (str): The ticker symbol for the asset.
    start_date (str): The start date in YYYY-MM-DD format.
    end_date (str): The end date in YYYY-MM-DD format.

    Returns:
    pd.DataFrame: DataFrame containing historical data or an empty DataFrame.
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if data.empty:
            logging.warning(f"No data found for {ticker} in the given date range.")
            return pd.DataFrame()
        return data
    except Exception as e:
        logging.error(f"Failed to download data for {ticker}: {e}")
        return pd.DataFrame()
