#!/usr/bin/python3
"""This module defines one function"""


def inherits_from(obj, a_class):
    """Checks if an object is a subclass of a class"""

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
