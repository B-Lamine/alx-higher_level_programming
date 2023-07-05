#!/usr/bin/python3

"""
This module contains add_integer function.
"""


def add_integer(a, b=98):
    """Compute sum of integers.

        Args:
            a (int): integer.
            b (int): by default b = 98.

        Returns:
            integer sum.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
