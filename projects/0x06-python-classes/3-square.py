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

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of the square

        Returns:
            The area of the square
        """

        return self.__size * self.__size
