#!/usr/bin/python3
"""This module contains the class BaseGeometry.
"""


class BaseGeometry:
    """Class with the method: area() and integer_validator.
    """
    def area(self):
        """Raise an exception with a message indicating this function is empty.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Raise error if value is not an integer, or <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
