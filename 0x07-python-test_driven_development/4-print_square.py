#!/usr/bin/python3

"""
This module contains the function print_square.
"""


def print_square(size):
    """Print a square as a sequence of '#'.

        Args:
            size (int): size of the square.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for height in range(size):
        print('#' * size)
