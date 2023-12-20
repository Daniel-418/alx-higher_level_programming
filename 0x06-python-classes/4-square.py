#!/usr/bin/python3
"""This module defines a square class"""


class Square:
    """
    A square class with one private attribute
    """

    def __init__(self, size=0):
        """
        initializes the class
        @param size: The size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        """
        returns the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size of the square
        @param value: the new size of the square
        """
        if type(value) is not int:
            raise TypeError("size muzt be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
