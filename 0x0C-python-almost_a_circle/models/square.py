#!/usr/bin/python3
"""This module contains the class: Square, which is a subclass of: Rectangle,
    which in turn is a subclass of: Base.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Square class constructor.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter method.
        """
        return self.width

    @size.setter
    def size(self, value):
        """size setter method.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """string formatted representation of the square class.
        """
        return "[Square] (" + str(self.id) + ") " + str(self.x) + "/" +\
            str(self.y) + " - " + str(self.width)
