#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Squares the element of a matrix
    :param matrix: Input matrix
    :return: A new matrix with each element squared
    """

    return [list(map(lambda x: x * x, row)) for row in matrix]
