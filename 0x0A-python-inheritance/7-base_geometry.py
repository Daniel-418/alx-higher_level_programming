#!/usr/bin/python3
"""The BaseGeometry class is defined in this module"""


class BaseGeometry:
    """An empty class"""

    def area(self):
        """A method that has not been implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a number"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
