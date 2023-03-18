#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_list = []
    for i in matrix:
        new_list.append(list(map(lambda x: x*x, i)))

    return new_list
