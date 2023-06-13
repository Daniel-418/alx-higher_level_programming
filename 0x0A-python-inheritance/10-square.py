#!/usr/bin/python3
"""Rectangle class that inherits from base geometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class"""

    def __init__(self, size):
        super().integer_validator("size", size)

        size.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
