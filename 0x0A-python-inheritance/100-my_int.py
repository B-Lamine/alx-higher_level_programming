#!/usr/bin/python3
"""This module contains the subclass MyInt of the class int.
"""


class MyInt(int):
    """Class MyInt with reverted __eq__ method.
    """
    def __init__(self, integer):
        """create integer object.
        """
        self.__integer = integer

    def __eq__(self, new_int):
        """CHeck if two integers are not equal.
        """
        return self.__integer != new_int

    def __ne__(self, new_int):
        """check if two integers are equal.
        """
        return self.__integer == new_int
