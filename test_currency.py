import unittest
from currency import CurrencyConverter


class TestCurrencyConverterInstantiation(unittest.TestCase):
    """
    Class used for testing the instantiation of the CurrencyConverter class from currency.py
    """
    # => To be filled


class TestCurrencyCheck(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.check_currencies() method from currency.py
    """
    # => To be filled


class TestReverseRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.reverse_rate() method from currency.py
    """
    # => To be filled


class TestRoundRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.round_rate() method from currency.py
    """
    # => To be filled


class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.get_historical_rate() method from currency.py
    """
    # => To be filled


if __name__ == '__main__':
    unittest.main()
