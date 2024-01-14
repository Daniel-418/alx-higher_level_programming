#!/usr/bin/python3
"""Defines a function that gets an object from a JSON string"""
import json


def from_json_string(my_str):
    """
    Gets back an object from a JSON string
    Args:
        my_str(str): The JSON representation of the object
    Returns:
        obj: The object represented by the JSON string.
    """
    return json.loads(my_str)
