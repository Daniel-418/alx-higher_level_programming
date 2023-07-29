#!/usr/bin/python3
"""MyInt class is defined here"""


class MyInt(int):
    """Creates the opposite version of an int class"""
    def __new__(cls, *args, **kwargs):
        """Initializes the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """inverts !="""
        return int(self) != other

    def __ne__(self, other):
        """inverts =="""
        return int(self) == other
