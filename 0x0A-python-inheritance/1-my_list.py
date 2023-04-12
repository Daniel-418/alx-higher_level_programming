#!/usr/bin/python3
"""Subclass of list"""

class MyList(list):
    """A subclass of list that contains a sorted method"""

    def __init__(self):
        super()

    def print_sorted(self):
        print(sorted(self))
