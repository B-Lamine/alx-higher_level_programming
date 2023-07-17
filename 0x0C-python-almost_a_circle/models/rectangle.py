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
        self.__y = y
