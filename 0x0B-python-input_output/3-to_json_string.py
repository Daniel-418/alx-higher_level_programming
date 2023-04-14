#!/usr/bin/python3
"""Contain method to encode JSON"""

import json


def to_json_string(my_obj):
    """returns the json representation of an object"""
    return json.dumps(my_obj)
