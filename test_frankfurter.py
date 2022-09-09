import unittest
from frankfurter import Frankfurter


class TestUrl(unittest.TestCase):
    """
    Class used for testing the url attributes of the Frankfurter class from frankfurter.py
    """
    def test_frankfurter_url_attributes(self):
        self.frankfurter = Frankfurter()
        self.assertEqual(self.frankfurter.base_url, "https://api.frankfurter.app")
        self.assertEqual(self.frankfurter.currencies_url, "https://api.frankfurter.app/currencies")
        self.assertEqual(self.frankfurter.historical_url, "")


class TestCurrenciesList(unittest.TestCase):
    """
    Class used for testing the currencies attribute of the Frankfurter class from frankfurter.py
    """
    def test_get_currencies_list(self):
        self.frankfurter = Frankfurter()
        self.assertIsNotNone(self.frankfurter.currencies)


class TestCheckCurrency(unittest.TestCase):
    """
    Class used for testing the Frankfurter.check_currency() method from frankfurter.py
    """
    def test_check_currency(self):
        self.frankfurter = Frankfurter()
        self.assertTrue(self.frankfurter.check_currency("AUD"))
        self.assertFalse(self.frankfurter.check_currency("aud"))


class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the Frankfurter.get_historical_rate() method from frankfurter.py
    """
    def test_get_historical_rate(self):
        self.frankfurter = Frankfurter()
        self.assertEqual(self.frankfurter.get_historical_rate("USD", "AUD", "2021-01-01"), 1.2954)


if __name__ == '__main__':
    unittest.main()
