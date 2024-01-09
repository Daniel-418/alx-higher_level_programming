#!/usr/bin/python3
"""Creates a sublist that inherits from the list class"""


class MyList(list):
    def print_sorted(self):
        """
        Prints the sorted version of this list
        """
        print(sorted(self))
