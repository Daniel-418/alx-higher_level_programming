#!/usr/bin/python3
"""This module contains the function to divide a matrix by
a number"""


def matrix_divided(matrix, div):
    """Divides a matrix by a particular number

        Args:
            matrix (list): The matrix to be divided
            div: The divisor

        Return:
            A new list populated with the result
        """

    new_list = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    inner_list = []
    for i in range(len(matrix)):
        inner_list = []
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a matrix" +
                            " (list of lists) of integers/floats")
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for j in matrix[i]:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
            else:
                inner_list.append(round(j / div, 2))

        new_list.append(inner_list)

    return new_list
