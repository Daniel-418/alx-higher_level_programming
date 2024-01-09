#!/usr/bin/python3
"""Defines a method to check if a class is a type of subtype"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a class or a subtype
    of a class.
    """
    return isinstance(obj, a_class)
