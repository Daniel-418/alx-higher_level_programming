#!/usr/bin/python3
"""This module contains the square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class"""
    def __init__(self, size):
        """Initializes the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
