#!/usr/bin/python3

"""
This module contains the function text_indentation.
"""


def text_indentation(text):
    """Prints a given string and replaces and adds double newlines
        when at each '.', '?' or ':'.

        Args:
            text (string): string input.
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    line = ''
    for c in text:
        if c in ['.', '?', ':']:
            if line[0] == " ":
                line = line[1:]
            if line[len(line)-1] == " ":
                line = line[:len(line)-1]
            line += c
            line += "\n\n"
            print(line, end='')
            line = ''
            continue
        line += c
