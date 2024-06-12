import unittest
from data_fetcher import fetch_data

class TestDataFetcher(unittest.TestCase):
    def test_fetch_data_valid(self):
        data = fetch_data('AAPL', '2023-01-01', '2023-12-31')
        self.assertIsNotNone(data)
        self.assertFalse(data.empty)

    def test_fetch_data_invalid(self):
        data = fetch_data('INVALID_TICKER', '2023-01-01', '2023-12-31')
        self.assertTrue(data.empty)

    def test_fetch_data_empty_date_range(self):
        data = fetch_data('AAPL', '2023-01-01', '2023-01-02')
        self.assertTrue(data.empty)

if __name__ == '__main__':
    unittest.main()
