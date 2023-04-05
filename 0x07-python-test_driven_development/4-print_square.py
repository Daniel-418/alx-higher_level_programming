#!/usr/bin/python3
"""Contains function to print a square"""


def print_square(size):
    """Prints a square of ``#`` based on the size given"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")

        if i != size - 1:
            print()
