#!/usr/bin/python3
"""This module contains the function: class_to_json.
"""


def class_to_json(obj):
    """get dictionary description of an object, without unserializable items.
    """
    tmp_dict = obj.__dict__
    dict_obj = {}
    for key in tmp_dict:
        if type(tmp_dict[key]) in [list, dict, str, int, bool]:
            dict_obj[key] = tmp_dict[key]
    return dict_obj
