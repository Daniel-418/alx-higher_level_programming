#!/usr/bin/python3
"""This module defines an empty class"""


class BaseGeometry:
    """defines a Base class for geometry"""

    def area(self):
        """missing implementation"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates an integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
