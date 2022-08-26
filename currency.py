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
        self.date = date

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
        frankfurter = Frankfurter()
        valid_from_currency = frankfurter.check_currency(self.from_currency)
        valid_to_currency = frankfurter.check_currency(self.to_currency)

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
        # => To be filled 

        Pseudo-code
        ----------
        # => To be filled 

        Returns
        -------
        # => To be filled 
        """
        # => To be filled 

    def round_rate(self, rate):
        """
        Method that will round an input argument to 4 decimals places.

        Parameters
        ----------
        # => To be filled 

        Pseudo-code
        ----------
        # => To be filled 

        Returns
        -------
        # => To be filled 
        """

        # => To be filled 

    def get_historical_rate(self):
        """
        Method that will call the Frankfurter API and get the historical conversion rate for the currencies (rounded to 4 decimals) and date stored in the class attributes.
        Then it will calculate the inverse rate and will exit by displaying the relevant message provided in the assignment brief

        Parameters
        ----------
        # => To be filled 

        Pseudo-code
        ----------
        # => To be filled 

        Returns
        -------
        # => To be filled 
        """

        # => To be filled 