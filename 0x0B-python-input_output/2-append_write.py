#!/usr/bin/python3
"""contains function to append text to a file"""


def append_write(filename="", text=""):
    """appends text to a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
