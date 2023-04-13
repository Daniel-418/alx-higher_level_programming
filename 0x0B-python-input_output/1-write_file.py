#!/usr/bin/python3
"""Contains the write_file function"""


def write_file(filename="", text=""):
    """function to write text to a file"""
    no_of_characters = 0
    with open(filename, 'w', encoding="utf-8") as f:
        no_of_characters = f.write(text)

    return no_of_characters
