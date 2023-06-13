#!/usr/bin/python3
"""Rectangle class that inherits from base geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
