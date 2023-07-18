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

    def update(self, *args, **kwargs):
        """update attributes depending on the number of arguments.
        """
        if len(args) == 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

    def __str__(self):
        """string formatted representation of the square class.
        """
        return "[Square] (" + str(self.id) + ") " + str(self.x) + "/" +\
            str(self.y) + " - " + str(self.width)
