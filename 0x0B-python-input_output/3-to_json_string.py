#!/usr/bin/python3
import json
"""This module returns the JSON representation of an object"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object
    Args:
        my_obj(any object): The object to be parsed into the JSON string
    Returns:
        str: The JSON representation of the object
    """
    return json.dumps(my_obj)
