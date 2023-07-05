#!/usr/bin/python3

"""
This module contains the function : matrix_divided.
"""


def matrix_divided(matrix, div):
    """Divide elements of a matrix.

        Args:
            matrix (int/float): list of lists of integers/floats.
            div (int/float): none zero integer/float.

        Return:
            matrix with results of elements division.
    """
    return_matrix = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for li in matrix:
        if type(li) != list:
            raise TypeError("matrix must be a matrix\
                    (list of lists) of integers/floats")
        if len(li) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        row = []
        for el in li:
            if type(el) not in [int, float]:
                raise TypeError("matrix must be a matrix\
                                (list of lists) of integers/floats")
            row += [round(el/div, 2)]
        return_matrix += [row]
    return return_matrix
