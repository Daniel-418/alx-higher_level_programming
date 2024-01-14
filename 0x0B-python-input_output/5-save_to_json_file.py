#!/usr/bin/python3
"""Defines a function that saves an object to a json file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Saves an object to a json file
    Args:
        my_obj: The object to be saved
        filename: The file to save the object to
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
