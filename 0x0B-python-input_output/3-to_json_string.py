#!/usr/bin/python3
"""Contains just one method"""
import json


def to_json_string(my_obj):
    """serializes an object to a json string"""
    return json.dumps(my_obj)
