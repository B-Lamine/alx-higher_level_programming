#!/usr/bin/python3
"""This module contains the function: load_from_json_file.
"""


from_json_string = __import__("4-from_json_string").from_json_string


def load_from_json_file(filename):
    """load object from json file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        my_obj = from_json_string(text)
    return my_obj
