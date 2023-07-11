#!/usr/bin/python3
"""This module contains function: add_item.
"""


import sys
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_item(filename="add_item.json"):
    """add command line argument to json file.
    """
    if not (os.path.isfile(filename)):
        list_obj = []
    else:
        list_obj = load_from_json_file(filename)
        for i in range(1, len(sys.argv)):
            list_obj.append(sys.argv[i])
    save_to_json_file(list_obj, filename)


if __name__ == '__main__':
    add_item()
