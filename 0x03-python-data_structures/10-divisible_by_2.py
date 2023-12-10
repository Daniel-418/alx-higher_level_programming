#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Checks if the elements in a list are divisible by 2
    :param my_list: Input list.
    :return: A new list that contains boolean values
    based on the original list
    """
    boolean_list = []

    if (my_list == []):
        return boolean_list

    for item in my_list:
        if (item % 2 == 0):
            boolean_list.append(True)
        else:
            boolean_list.append(False)

    return boolean_list
