#!/usr/bin/python3
"""Defines a method to check if an instance is a subclass of a type"""


def inherits_from(obj, a_class):
    """
    Checks if an instance is a subclass of a type
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
