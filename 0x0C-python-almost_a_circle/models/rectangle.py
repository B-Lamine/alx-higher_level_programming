#!/usr/bin/python3
"""This module contains the class: Rectangle, which is a subclass of Base.
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class, with attributes:
        width, height, x, y and id.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiation method.
        """
        for attr, value in locals().items():
            if (attr in ['width', 'height', 'x', 'y']) and (type(value)
                                                            != int):
                raise TypeError("{} must be an integer".format(attr))
            if (attr in ['width, height']) and (value <= 0):
                raise ValueError("{} must be > 0".format(attr))
            if (attr in ['x', 'y']) and (value < 0):
                raise ValueError("{} must be >= 0".format(attr))
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter method
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width stter method
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter method
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter method
        """
        return self.__x

    @x.setter
    def x(self, value):
        """x setter method
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter method
        """
        return self.__y

    @y.setter
    def y(self, value):
        """y setter method
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
