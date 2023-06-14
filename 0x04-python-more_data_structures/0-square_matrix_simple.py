#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square_matrix = []
    for row in matrix:
        square_row = []
        for element in row:
            square_row += [element * element]
        square_matrix += [square_row]
    return square_matrix
