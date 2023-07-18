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

    @classmethod
    def save_to_file(cls, list_objs):
        """convert list of instances to json dictionary and save to file.
        """
        if list_objs is None:
            json_dict = "[]"
        else:
            list_objs_dict = [obj.to_dictionary() for obj in list_objs]
            json_dict = cls.to_json_string(list_objs_dict)
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json_dict)
