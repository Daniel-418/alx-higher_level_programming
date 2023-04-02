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

    @property
    def size(self):
        """Retrieves the size of this square

        Returns:
            The size of this square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of the size of this square

        Args:
            value (int): The value to assign to this square's size

        Return:
            void
        """

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square

        Return:
            The area of the square
        """

        return self.__size * self.__size

    def my_print(self):
        """Prints a square to the standard output

        Return:
            void
        """

        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
