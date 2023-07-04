#!/usr/bin/python3

"""
This method contains the simplest Rectangle class
"""


class Rectangle:
    """
        define Rectangle.

        Attributes:
            number_of_instances (int): number of objects created.
            print_symbol (any type): object used to print rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            instantiation method.

            Args:
                width (integer, optional): width of the rectangle.
                height (integer, optional: height of the rectange)
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    def __del__(self):
        """Print message upon instance deletion """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """integer: get width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """integer: get height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """Public instance method for computing rectangle's perimeter.

            Returns:
                rectangle's perimeter.
        """
        if (self.__height == 0) or (self.__width == 0):
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def area(self):
        """Public instance method for computing rectangle's area.

            Returns:
                rectangle's area.
        """
        return self.__height * self.__width

    def __str__(self):
        """str: sequences of print_symbol width times, over height times line
        """
        if (self.__height == 0) or (self.__width == 0):
            return ''
        else:
            return (str(self.print_symbol) * self.__width + '\n') *\
                (self.__height - 1) + (str(self.print_symbol) *
                                       self.__width)

    def __repr__(self):
        """string representation of the rectangle"""
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) +\
            ")"
