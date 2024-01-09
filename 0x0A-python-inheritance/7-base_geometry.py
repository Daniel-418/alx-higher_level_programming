#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry:
    """A BaseGeometry parent class"""
    def area(self):
        """
        Not yet implemented.
        Raises:
            Exception: Gives a warning message that the method is not yet
            implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer value
        Args:
            name(string): The name of the value to be validated.
            value(int): The value to be validated
        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less than or equal to zero
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
