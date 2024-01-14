#!/usr/bin/python3
"""This file contains a method that reads a file"""


def read_file(filename=""):
    """
    Reads a file and outputs it's content to the standard output.
    Args:
        filename(str): The name of the file to be read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())
