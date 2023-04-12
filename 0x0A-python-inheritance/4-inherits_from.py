#!/usr/bin/python3

def inherits_from(obj, a_class):
    """checks if an objects inherits from a class"""

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
