#!/usr/bin/python3
"""contains one method"""
import json


def class_to_json(obj):
    return obj.__dict__
