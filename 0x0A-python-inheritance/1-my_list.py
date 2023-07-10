#!/usr/bin/python3
"""This module contains a subclass of List class: MyList
"""


class MyList(list):
    def print_sorted(self):
        """print sorted list.
        """
        print(sorted(self, reverse=False))
