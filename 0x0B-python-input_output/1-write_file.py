#!/usr/bin/python3
"""This module contains the function: write_file.
"""


def write_file(filename="", text=""):
    """write string to file, overwrite if latter exists.
        Return number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        character_number = f.write(text)
        return character_number
