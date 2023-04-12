#!/usr/bin/python3
"""The Rectangle class is defined in this module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class"""

    def __init__(self, width, height):
        """initializes a Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """A method that has not been implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a number"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
