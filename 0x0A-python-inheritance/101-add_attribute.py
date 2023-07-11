#!/usr/bin/python3
"""This module contains the function add_attribute.
"""


def add_attribute(obj, name, value):
    """Check if attribute can be added to obj.
        Set it if true, otherwise raise TypeError.
    """
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
