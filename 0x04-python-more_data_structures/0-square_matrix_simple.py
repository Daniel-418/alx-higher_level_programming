#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Squares the element of a matrix
    :param matrix: Input matrix
    :return: A new matrix with each element squared
    """
    final_list = []
    square = lambda x: x * x

    return [list(map(square, row)) for row in matrix]
