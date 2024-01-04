#!/usr/bin/python3
"""This is the add integer module"""


def add_integer(a, b=98):
    """
    add_integer: adds two integers together
    @param: a: The first integer
    @param: b: The second integer

    Return: Addition of the two integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
