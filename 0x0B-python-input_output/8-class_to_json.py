#!/usr/bin/python3
"""contains the method"""

def class_to_json(obj):
    """returns the dictionary representation of an object"""
    return obj.__dict__
