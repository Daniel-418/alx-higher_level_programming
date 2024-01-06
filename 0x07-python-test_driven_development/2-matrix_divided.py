#!/usr/bin/python3
"""Contains the matrix_divided function that divides the element of a matrix"""


def matrix_divided(matrix, div):
    """
    Divides each element of a given matrix by a specified divisor

    This function performs an element-wise division of a matrix by a divisor
    rounding each result to two decimal places.

    Args:
        matrix (list of lists of int/float): The matrix to be divided
        div (int/float): The divisor

    Returns:
        list of lists of float: A new matrix containing the results
                                of the division

    Raises:
        TypeError: if the matrix elements are not list of integers/floats or
                if div is not 0
        ZeroDivisionError: If div is zero.
        TypeError: If rows of the matrix are of inconsistent size.
    """
    row_size = 0
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix(list of lists) of" +
                            " integers/floats")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix(list of lists) of" +
                                " integers/floats")

    row_size = len(matrix[0])
    for i in matrix:
        if len(i) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    return [[round(element / div, 2) for element in row] for row in matrix]
