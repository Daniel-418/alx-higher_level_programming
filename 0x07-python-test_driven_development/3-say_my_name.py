#!/usr/bin/python3
"""A function that says the user name"""


def say_my_name(first_name, last_name=""):
    """
    Prints the given first and last name of the input
    Args:
        first_name (string): The first name to be printed
        last_name (string): The last name to be printed

    Returns:
        void: It doesn't return anything
    Raises:
        TypeError: If the first or last na e is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
