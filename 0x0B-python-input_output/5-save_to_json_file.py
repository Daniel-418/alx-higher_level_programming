#!/usr/bin/python3
"""Contains save_to_json_file() function"""

import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
