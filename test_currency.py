import unittest
from currency import CurrencyConverter


class TestCurrencyConverterInstantiation(unittest.TestCase):
    """
    Class used for testing the instantiation of the CurrencyConverter class from currency.py
    """

    def test_instantiate_currency_converter(self):
        currency_converter = CurrencyConverter("USD", "AUD", "2021-01-01")
        message = "Given object is not instance of CurrencyConverter."

        self.assertIsInstance(currency_converter, CurrencyConverter, message)


class TestCurrencyCheck(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.check_currencies() method from currency.py
    """
    def test_check_currencies(self):
        self.currency_converter = CurrencyConverter("USD", "AUD", "2021-01-01")
        self.assertIsNone(self.currency_converter.check_currencies())


class TestReverseRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.reverse_rate() method from currency.py
    """
    def test_reverse_rate(self):
        self.currency_converter = CurrencyConverter("USD", "AUD", "2021-01-01")
        self.currency_converter.rate = 1.2954
        self.currency_converter.reverse_rate()
        self.assertEqual(self.currency_converter.inverse_rate, 0.772)


class TestRoundRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.round_rate() method from currency.py
    """
    def test_round_rate(self):
        self.currency_converter = CurrencyConverter("USD", "AUD", "2021-01-01")
        self.assertEqual(self.currency_converter.round_rate(32.3232323), 32.3232)


class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.get_historical_rate() method from currency.py
    """
    def test_get_historical_rate(self):
        self.currency_converter = CurrencyConverter("USD", "AUD", "2021-01-01")
        self.assertIsNone(self.currency_converter.get_historical_rate())


if __name__ == '__main__':
    unittest.main()
