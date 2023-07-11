#!/usr/bin/python3
"""This module contains the function: save_to_json_file.
"""


to_json_string = __import__("3-to_json_string").to_json_string


def save_to_json_file(my_obj, filename):
    """convert object to json string and write it to file.
    """
    text = to_json_string(my_obj)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
