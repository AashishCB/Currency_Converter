from api import call_get


class Frankfurter:
    """
    Class that manages API calls to Frankfurter. It will be used to store the URLS to the relevant endpoints. It will also automatically call the Currencies endpoint and store the return list of available currency codes.

    Attributes
    ----------
    base_url : str
        Base url to Frankfurter API
    currencies_url : str
        Frankfurter endpoint for extracting currencies list
    historical_url : str
        Frankfurter endpoint for extracting historical currencies conversion rates
    currencies: list
        List of available currency codes
    """

    def __init__(self):
        self.base_url = "https://api.frankfurter.app"
        self.currencies_url = F"{self.base_url}/currencies"
        self.historical_url = ""
        self.currencies = self.get_currencies_list()

    def get_currencies_list(self):
        """
        Method that will get the list of available currencies and returns it as a Python list.

        Parameters
        ----------
        self : Frankfurter
            An object from Frankfurter class

        Pseudo-code
        ----------
        Call the currencies endpoint and store the response
        Extract json data
        Store the currency codes from json data to currencies

        Returns
        -------
        currencies => list
             List of available currency codes
        """
        response = call_get(self.currencies_url)
        data = response.json()
        currencies = data.keys()
        return currencies

    def check_currency(self, currency):
        """
        Method that will check if a provided currency code is valid and return True if that is the case.
        Otherwise it will return False.

        Parameters
        ----------
        currency : str
            Code for the currency

        Pseudo-code
        ----------
        Search if currency is in the currencies_list

        Returns
        -------
        True : bool
        """
        return True if currency in self.currencies else False

    def get_historical_rate(self, from_currency, to_currency, from_date, amount=1):
        """
        Method that will call the historical API endpoint in order to get the conversion rate for a given dates and currencies. It will return an requests.models.Response object.

        Parameters
        ----------
        from_currency : str
            Code for the origin currency
        to_currency : str
            Code for the destination currency
        from_date : str
            Date when the conversion rate was recorded
        amount : int
            Optional parameter with default value 1

        Pseudo-code
        ----------
        Call the currencies endpoint and store the response
        Extract json data
        Fetch the destination currency conversion rate from json

        Returns
        -------
        rate : float
        """
        self.historical_url = F"{self.base_url}/{from_date}?from={from_currency}&to={to_currency}"
        response = call_get(self.historical_url)
        response_data = response.json()
        return response_data['rates'][to_currency]
