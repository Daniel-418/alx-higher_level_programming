#!/usr/bin/python3
"""Defines a method to check if an obj is the same instance of the other"""


def is_same_class(obj, a_class):
    if (type(obj) == a_class):
        return True
    else:
        return False
