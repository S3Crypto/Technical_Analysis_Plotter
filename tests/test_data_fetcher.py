import unittest
from data_fetcher import fetch_data

class TestDataFetcher(unittest.TestCase):
    def test_fetch_data(self):
        data = fetch_data('AAPL', '2023-01-01', '2023-12-31')
        self.assertIsNotNone(data)
        self.assertFalse(data.empty)

if __name__ == '__main__':
    unittest.main()