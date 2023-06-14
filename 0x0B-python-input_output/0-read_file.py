#!/usr/bin/python3
"""This module reads a text file"""


def read_file(filename=""):
    """method to read content of a file and print"""

    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
