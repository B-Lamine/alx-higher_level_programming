#!/usr/bin/python3
"""This module contains the subclass Square of the class Rectangle, which is
    a subclass of the class BaseGeometry.
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Define a square with area and string format.
    """
    def __init__(self, size):
        """initiate a square object.
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """compute area of the square.
        """
        return self.__size * self.__size
