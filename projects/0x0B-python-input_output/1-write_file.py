#!/usr/bin/python3
"""This module defines a method to write to a file"""


def write_file(filename="", text=""):
    """This method writes text to a file"""

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
