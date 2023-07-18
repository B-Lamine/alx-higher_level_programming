#!/usr/bin/python3
"""This module contains the class: Base.
"""

import json


class Base:
    """Base class that manages id of all subclasses/objects.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiation method for the Base class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert list of dictionaries into a json string.
        """
        if (list_dictionaries is None) or (len(list_dictionaries) == 0):
            return "[]"
        return json.dumps(list_dictionaries)
