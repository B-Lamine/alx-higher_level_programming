#!/usr/bin/python3
"""This module contains the function is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance the given class or one its parent
        classes.
    """
    return isinstance(obj, a_class)
