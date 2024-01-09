#!/usr/bin/python3
"""Contains a rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A representation of a rectangle"""
    def __init__(self, width, height):
        """
        Constructor for the Rectangle class
        Args:
            width(int): Width of the rectangle.
            height(int): height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of this rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Represents a readable representation of this rectangle
        Returns:
            str: A string representation of this rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
