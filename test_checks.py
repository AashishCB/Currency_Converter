import unittest
from checks import check_arguments, check_date


class TestCheckArguments(unittest.TestCase):
    """
    Class used for testing the check_arguments() function from checks.py
    """
    def test_check_arguments(self):
        self.assertEqual(check_arguments(["2021-01-01", "GBP", "AUD"]), ["2021-01-01", "GBP", "AUD"])
        self.assertIsNone(check_arguments([]))
        self.assertIsNone(check_arguments(["2021-01-01"]))
        self.assertIsNone(check_arguments(["2021-01-01", "AUD"]))
        self.assertIsNone(check_arguments(["2021-01-01", "AUD", "EUR", "GBP"]))


class TestCheckDate(unittest.TestCase):
    """
    Class used for testing the check_date() function from checks.py
    """
    def test_check_date(self):
        self.assertTrue(check_date("2021-01-01"))
        self.assertIsNone(check_date("2022/01/01"))
        self.assertIsNone(check_date("2022-01-41"))


if __name__ == '__main__':
    unittest.main()
