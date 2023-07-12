#!/usr/bin/python3
"""This module contains the class: Student.
"""


class Student:
    """Student class, with to_json method.
    """
    def __init__(self, first_name, last_name, age):
        """instantiate Student's first_name, last_name, age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """get dictionary description of Student.
        """
        tmp_dict = self.__dict__
        dict_obj = {}
        if attrs is not None:
            for key in tmp_dict:
                if key in attrs:
                    dict_obj[key] = tmp_dict[key]
        else:
            for key in tmp_dict:
                if type(tmp_dict[key]) in [list, dict, str, int, bool]:
                    dict_obj[key] = tmp_dict[key]
        return dict_obj

    def reload_from_json(self, json):
        """reset object attributes according to json file.
        """
        for key in json:
            if key in json:
                self.__dict__[key] = json[key]
