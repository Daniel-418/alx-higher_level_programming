#!/usr/bin/python3
"""Defines a method to check if an obj is the same instance of the other"""


def is_same_class(obj, a_class):
    """
    Checks if an object is the same class.
    Args:
        obj(object): the object
        a_class(class): the class
    """
    if (type(obj) == a_class):
        return True
    else:
        return False
