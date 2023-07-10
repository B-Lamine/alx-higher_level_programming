#!/usr/bin/python3
"""This module contains the function is_same_class.
"""


def is_same_class(obj, a_class):
    """Check if object is an instance the given class.
    """
    return type(obj) == a_class
