#!/usr/bin/python3

"""
This module contains the function: say_my_name.
"""


def say_my_name(first_name, last_name=""):
    """Print given full name.

        Args:
            first_name (str): first name.
            last_name (str): last name, empty by default.
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
