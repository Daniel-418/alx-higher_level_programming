#!/usr/bin/python3
"""contains one method"""
import json


def class_to_json(obj):
    """Returns a dictionary representation of an object"""
    return obj.__dict__
