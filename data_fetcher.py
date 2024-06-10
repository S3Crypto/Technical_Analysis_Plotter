import yfinance as yf

def fetch_data(ticker, start_date, end_date):
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if data.empty:
            raise ValueError(f"No data found for {ticker} in the given date range.")
        return data
    except Exception as e:
        print(f"Failed to download data for {ticker}: {e}")
        return None
        