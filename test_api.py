import unittest
from unittest.mock import patch, MagicMock

from api import call_get


class TestAPI(unittest.TestCase):
    """
    Class used for testing the call_get() function in api.py
    """
    def test_call_get(self):
        self.assertIsNotNone(call_get("https://api.frankfurter.app/currencies"))


if __name__ == '__main__':
    unittest.main()
