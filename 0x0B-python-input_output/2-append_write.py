#!/usr/bin/python3
"""This module contains the function: append_write.
"""


def append_write(filename="", text=""):
    """append string to file.
        Return number of characters appended.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        character_number = f.write(text)
    return character_number
