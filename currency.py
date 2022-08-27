import sys
from frankfurter import Frankfurter


class CurrencyConverter:
    """
    Class that represents a Currency conversion object. It will be used to store the input arguments (currency codes, date) and also other information required (amount, rate, inverse rate, instantiation of Frankfurter class).

    Attributes
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    rate : float
        The conversion rate to be applied on the origin amount (origin -> destination)
    inverse_rate : float
        The inverse of the previous rate  (destination -> origin)
    date : str
        Date when the conversion rate was recorded
    api : Frankfurter
        Instance of Frankfurter class
    """
    def __init__(self, from_currency, to_currency, date):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = float()
        self.rate = float()
        self.inverse_rate = float()
        self.date = date
        self.api = Frankfurter()

    def check_currencies(self):
        """
        Method that will check if currency codes stored in the class attributes are valid.
        Otherwise the program will exit and display the relevant message provided in the assignment brief

        Parameters
        ----------
        self : CurrencyConverter
            An object of CurrencyConverter class

        Pseudo-code
        ----------
        Instantiate an objet from your defined Frankfurter class
        Check the validity of the 2 currency codes (using your defined check_currency() method from Frankfurter class)
        """
        valid_from_currency = self.api.check_currency(self.from_currency)
        valid_to_currency = self.api.check_currency(self.to_currency)

        if not (valid_from_currency or valid_to_currency):
            print(F"{self.from_currency} and {self.to_currency} are not valid currency codes")
            exit()
        elif not valid_from_currency:
            print(F"{self.from_currency} is not a valid currency code")
            exit()
        elif not valid_to_currency:
            print(F"{self.to_currency} is not a valid currency code")
            exit()

    def reverse_rate(self):
        """
        Method that will calculate the inverse rate from the value stored in the class attribute, round it to 4 decimal places and save it back in the class attribute inverse_rate.

        Parameters
        ----------
        self : CurrencyConverter
            An object of CurrencyConverter class

        Pseudo-code
        ----------
        Inverse the number with reciprocal way
        Round it off to four decimal places
        Store in the class attribute self.inverse_rate
        """
        inverse_rate = 1.0/self.rate
        self.inverse_rate = self.round_rate(inverse_rate)

    def round_rate(self, rate):
        """
        Method that will round an input argument to 4 decimals places.

        Parameters
        ----------
        rate : float
            The conversion rate to be applied to a couple of currency codes

        Pseudo-code
        ----------
        Round off rate to 4 decimal places(using built-in round())

        Returns
        -------
        rounded_rate : float
        """
        rounded_rate = round(rate, 4)
        return rounded_rate

    def get_historical_rate(self):
        """
        Method that will call the Frankfurter API and get the historical conversion rate for the currencies (rounded to 4 decimals) and date stored in the class attributes.
        Then it will calculate the inverse rate and will exit by displaying the relevant message provided in the assignment brief

        Parameters
        ----------
        self : CurrencyConverter
            An object of CurrencyConverter class.

        Pseudo-code
        ----------
        Extract the historical rate(using self.api.get_historical_rate() of Frankfurter class)
        Round up to 4 decimal places(using self.round_rate())
        Fetch the inverse rate(using self.reverse_rate())

        Returns
        -------
        rate : float
        """
        historical_rate = self.api.get_historical_rate(self.from_currency, self.to_currency, self.date)
        self.rate = self.round_rate(historical_rate)
        self.reverse_rate()
        print(F"The conversion rate on {self.date} from {self.from_currency} to {self.to_currency} was {self.rate}."
              F"The inverse rate was {self.inverse_rate}")
