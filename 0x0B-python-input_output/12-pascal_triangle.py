#!/usr/bin/python3
"""This module contains the function: pascal_triangle.
"""


def pascal_triangle(n):
    """make the pascal triangle as a list of lists.
    """
    pascal_triangle = [[1], [1, 1]]
    tmp_list = [1, 1]
    for i in range(2, n):
        next_list = [1, 1]
        next_list[1:len(next_list)-1] = [tmp_list[j+1] + tmp_list[j]
                                         for j in range(len(tmp_list) - 1)]
        pascal_triangle.append(next_list)
        tmp_list = next_list
    return pascal_triangle
