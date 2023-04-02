#!/usr/bin/python3
"""Creates a square with size attribute"""


class Square:
    """A class representing a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor to initialize the square

        Args:
            size (int): The size of the square.
            position (tuple): The x and y coordinate of the square

        Returns:
            A square object
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if Square.__validate_position(position):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def __validate_position(position=(0, 0)):
        """Helper function to validate that the position
        consists of just two positive integers

        Args:
            position (tuple): The tuple to be validated

        Return:
            True (boolean): If the tuple is valid
            False (boolean): If the tuple is invalid
        """

        if type(position) == tuple and len(position) == 2:
            if position[0] >= 0 and position[1] >= 0:
                return True
            else:
                return False
        else:
            return False

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

    @property
    def position(self):
        """Retrieves the position of this square

        Returns:
            The position of this square
        """

        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of this square

        Args:
            value (tuple): The value to set this position
        """

        if Square.__validate_position(value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
            return

        for i in range(0, self.__position[1]):
            print()

        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
            print()
