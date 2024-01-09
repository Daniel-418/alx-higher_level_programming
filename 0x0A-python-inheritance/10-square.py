#!/usr/bin/python3
"""Defines a square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines a square
    """
    def __init__(self, size):
        """
        Constructor for this square
        """
        super().__init__(size, size)
