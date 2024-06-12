import yfinance as yf
import logging

logging.basicConfig(level=logging.INFO)

def fetch_data(ticker, start_date, end_date):
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if data.empty:
            raise ValueError(f"No data found for {ticker} in the given date range.")
        return data
    except Exception as e:
        logging.error(f"Failed to download data for {ticker}: {e}")
        return None
