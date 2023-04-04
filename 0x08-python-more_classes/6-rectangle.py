#!/usr/bin/python3
"""This module defines a Rectangle class"""


class Rectangle:
    """This class defines an empty Rectangle object"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Constructor for the Rectangle object

        Args:
            width (int): The width of the Rectangle
            height (int): The height of the Rectangle

        Return: A Rectangle object
        """

        if (Rectangle.__validate_parameter(width, "width") and
                Rectangle.__validate_parameter(height, "height")):
            self.__width = width
            self.__height = height
            Rectangle.number_of_instances += 1

    @staticmethod
    def __validate_parameter(parameter, string):
        """Utility method to validate the values passed
            as the object's attributes

        Args:
            parameter (int): The number to be validated
            string (str): The string representation of the parameter to pass
                            to the error message

            Return: True if the parameter is valid. False if otherwise
        """

        if type(parameter) is not int:
            raise TypeError(string + " must be an integer")
            return False
        elif parameter < 0:
            raise ValueError(string + " must be >= 0")
            return False
        else:
            return True

    @property
    def width(self):
        """Width property to set and get the width value of this Rectangtle"""

        return self.__width

    @width.setter
    def width(self, value):
        if Rectangle.__validate_parameter(value, "width"):
            self.__width = value

    @property
    def height(self):
        """Height property to set and get the height value of this Rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        if Rectangle.__validate_parameter(value, "height"):
            self.__height = value

    def area(self):
        """Calculates the area of this Rectangle

        Returns: The area of the rectangle
        """

        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of this Rectangle

        Returns: The perimeter of this rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of this rectangle"""

        new_string = ""

        if self.__width == 0 or self.__height == 0:
            return new_string

        for i in range(0, self.__height):
            for j in range(0, self.__width):
                new_string = new_string + "#"
            if i != self.__height - 1:
                new_string = new_string + "\n"

        return new_string

    def __repr__(self):
        """Returns an offical string representation of this rectangle"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes this rectangle"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
