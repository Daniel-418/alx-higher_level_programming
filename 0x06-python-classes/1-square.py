#!/usr/bin/python3
"""Creates a square with size attribute"""


class Square:
    """A class representing a square"""

    def __init__(self, size=0):
        """Constructor to initialize the square

        Args:
            size (int): The size of the square.

        Returns:
            A square object
        """

        self.__size = size
