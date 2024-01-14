#!/usr/bin/python3
"""Defines a function that loads a json object from file"""
import json


def load_from_json_file(filename):
    """
    Loads a json object from a file
    Args:
        filename(str): The name of the file.
    Return:
        obj: The object created from the json representation in the file
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        obj = json.load(f)

    return obj
