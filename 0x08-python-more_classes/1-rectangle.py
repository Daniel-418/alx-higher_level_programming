#!/usr/bin/python3
"""A module to define a rectangle class"""


class Rectangle:
    """defines the rectangle class"""

    def __init__(self, width=0, height=0):
        """initializes the class"""
        if height < 0 or width < 0:
            raise ValueError("Height and width must be >= 0")
        if type(height) is not int or type(width) is not int:
            raise TypeError("Height and width must be an integer")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the value for the height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height
