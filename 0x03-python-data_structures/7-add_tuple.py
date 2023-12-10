#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples together
    :param tuple_a: First tuple.
    :param tuple_b: Second tuple.
    :return: Tuple containing the element-wise sum
    """
    result = ()
    first_element = 0
    second_element = 0
    tuple_a = validate(tuple_a)
    tuple_b = validate(tuple_b)

    first_element = tuple_a[0] + tuple_b[0]
    second_element = tuple_a[1] + tuple_b[1]

    result = (first_element, second_element)
    return result


def validate(a_tuple):
    """
    Ensures the tuples has two element
    :param a_tuple: Input tuple.
    :return: Tuple with two elements.
    """
    a_tuple_len = len(a_tuple)

    if (a_tuple_len == 0):
        return (0, 0)
    elif (a_tuple_len == 1):
        return a_tuple[0], 0
    else:
        return a_tuple[0], a_tuple[1]
