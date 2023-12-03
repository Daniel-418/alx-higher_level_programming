#!/usr/bin/python3
"""This module adds two integers"""

from add_0 import add


def main():
    """
    main - adds two integers

    Return: void
    """
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))


if __name__ == "__main__":
    main()
