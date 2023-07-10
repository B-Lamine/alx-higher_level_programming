#!/usr/bin/python3
"""This module contains the function: lookup.
"""


def lookup(obj):
    """List available attributes of an object.
    """
    return list(type(obj).__dict__)
