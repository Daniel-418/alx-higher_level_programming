#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Finds the maximum value of a list
    :param my_list: The input list
    :return: The maximum value of the list
    """
    maximum = 0

    if (len(my_list) == 0):
        return None

    for item in my_list:
        if (item > maximum):
            maximum = item

    return maximum
