import requests
import sys

from requests import HTTPError


def call_get(url: str) -> requests.models.Response:
    """
    Function that will call the API endpoint (input parameter) and return its response as a requests.models.Response object
    In case of an error, the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    url : str

    Pseudo-code
    ----------
    Make the relevant api call

    Returns
    -------
    response : requests.models.Response
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except HTTPError as e:
        print("There is an error with Frankfurter API")
        exit()
