#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, column in enumerate(row):
            if i == len(row) - 1:
                print("{:d}".format(column))
            else:
                print("{:d}".format(column), end=" ")
