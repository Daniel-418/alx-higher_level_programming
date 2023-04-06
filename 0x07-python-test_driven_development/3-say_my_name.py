#!/usr/bin/python3
"""This module contains a function used to print the user's name 
on the command line
"""

def say_my_name(first_name, last_name=""):
    """Function to print the user's name on the command line"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is", first_name, last_name)
