#!/usr/bin/python3

"""
This module contains a class that defines a square
"""


class Square:
    """
    class of squares.
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size * self.__size)
