#!/usr/bin/python3
"""This module contains the class: Base.
"""


class Base:
    """Base class that manages id of all subclasses/objects.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiation method for the Base class.
        """
        if id not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
