#!/usr/bin/python3
"""defines a class that inherits from list"""


class MyList(list):
    """This class inherits from my list"""

    def __init__(self):
        """initializes the class"""
        super()

    def print_sorted(self):
        """method to print the sorted list"""
        print(sorted(self))
