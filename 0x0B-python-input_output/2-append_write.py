#!/usr/bin/python3
"""Defines a function that appends text to a file"""


def append_write(filename="", text=""):
    """
    Appends text to the end of a file.
    Args:
        filename(str): The name of the file to be manipulated
        text(str): The text to be appended to the end of the file
    Returns:
        int: The number of characters appended to the file
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        nb = f.write(text)

    return nb
