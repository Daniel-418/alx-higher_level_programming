#!/usr/bin/python3
"""This module defines a function that can print square using asteriks"""


def print_square(size):
    """
    A function to print a square of specified size
    Args:
        size (int): The size of the square
    Returns:
        void
    Raises:
        TypeError: If the size is not an integer
        ValueError: If the size is negative
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
