#!/usr/bin/python3
"""Contains the read_file function"""


def read_file(filename=""):
    """function that reads the entire string of a text file"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
