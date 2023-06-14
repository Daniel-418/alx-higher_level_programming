#!/usr/bin/python3
"""This module contains just one function"""
import json


def save_to_json_file(my_obj, filename):
    """saves to a json file"""
    with open(filename, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(my_obj))
