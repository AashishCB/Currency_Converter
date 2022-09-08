import datetime
import sys


def check_arguments(args):
    """
    Function that will check if there are enough input arguments provided (ie exactly 3) and will return the input arguments if it is the case.
    Otherwise, the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    args : list
        List containing a date and two currency codes

    Pseudo-code
    ----------
    Check there are 3 items in the input argument

    Returns
    -------
    args : list
        List containing a date and two currency codes
    """

    if len(args) == 3:
        return args
    print("[ERROR] You need to provide 3 arguments in the following order: <date> <currency1> <currency2>")


def check_date(date):
    """
    Function that will check if the provided date is valid and will return the value True if that is the case.
    Otherwise, the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    date : str

    Pseudo-code
    ----------
    Convert the given date string to datetime using strptime() function

    Returns
    -------
    True : bool
    """
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError as e:
        print("Provided date is invalid")
