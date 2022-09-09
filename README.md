# Currency Converter

## Author
Name: Aibarna Singh Basnet

Student ID: 24585717 

## Description
### What your application does
This program simply manifests the use of API to enable the end user the conversion and inverse conversion between 2 currencies on a particular date using frankfurter open-source API.

### Some of the challenges you faced
- Getting started in using API

- Grasping the concepts of objects in python

- Research and implementation of test case

### Some of the features you hope to implement in the future

- Implement a subscription based model to alert subscribers about potential profit on the exchange rate

- Provide an interface to display nearby money exchange center and their exchange rate

## How to Setup
- Download and extract the contents of the zipped file

- Verify that python is installed on the system

<Provide a step-by-step description of how to get the development environment set and running.>

**Set up a virtual environment:**

` python3 -m venv /path/to/new/virtual/environment. `

**Install external python module using:**

 ` pip install requests `

###### Which Python version you used
**python version - 3.8.9**


### packages and version you used

- certifi==2022.6.15
- charset-normalizer==2.1.1
- idna==3.3
- requests==2.28.1
- urllib3==1.26.12

## How to Run the Program
     python3 main.py $date $currency_code_1 $currency_code_2 

## Project Structure
main.py - Contains the main logics of the program from handling input to calling validation functions

checks.py - Contains 2 validations for checking arguments and validating date

api.py- Contains function that calls the given API endpoint using request module to fetch response and raise error in case of failure

frankfurter.py - Contains method to get historical rates for given currency codes for a given date

currency.py - Contains CurrencyConverter class to handle the reverse and round off of the fetched rates from the API endpoint

test_checks.py - Tests validation methods from checks.py

test_frankfurter.py - Tests Frankfurt class attributes and validation methods from frankfurter.py

test_api.py - Tests the requests module for various given endpoints and raises error for failure response or no response

test_currency.py - Tests the CurrencyConverter Instances and its methods for currency.py

README.md - Provides the documentation for the currency converter app

## Citations
Unittest — Unit Testing Framework — Python 3.10.7 Documentation. https://docs.python.org/3/library/unittest.html. Accessed 9 Sept. 2022.

Python Requests Module. https://www.w3schools.com/python/module_requests.asp. Accessed 9 Sept. 2022.