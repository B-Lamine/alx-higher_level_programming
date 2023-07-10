#!/usr/bin/python3
"""This module contains the subclass Rectangle of the class BaseGeometry.
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Define a Rectangle class.
    """
    def __init__(self, width, height):
        """initiate a Rectangle object.
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
