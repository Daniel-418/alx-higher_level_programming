#!/usr/bin/python3
"""This module contains just one function"""
import json


def load_from_json_file(filename):
    """loads from a json file"""
    with open(filename, 'r', encoding='utf-8') as json_file:
        return json.load(f)
