#!/usr/bin/python3
"""This module contains the function inherits_from.
"""


def inherits_from(obj, a_class):
    """Check if object is an instance of a subclass of the given class.
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
