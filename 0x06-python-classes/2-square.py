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
