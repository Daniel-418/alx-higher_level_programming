#!/usr/bin/python3
"""This module defines a function to write a str to a file"""


def write_file(filename="", text=""):
    """
    Writes a text to a file. Overrides it's content if it exists
    and creates a new file if it doesn't
    Args:
        filename(str): The name of the file the text is to be written to
        text(str): The text to be written to the file
    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        number_of_characters = f.write(text)

    return number_of_characters
