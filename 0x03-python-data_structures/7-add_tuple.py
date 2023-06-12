#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_add = ()
    for i in range(2):
        if i < len(tuple_a) and i < len(tuple_b):
            tuple_add += tuple_a[i] + tuple_b[i],
        elif i < len(tuple_a) and i >= len(tuple_b):
            tuple_add += tuple_a[i],
        elif i >= len(tuple_a) and i < len(tuple_b):
            tuple_add += tuple_b[i],
        else:
            tuple_add += (tuple_a[i] + tuple_b[i]),
    return tuple_add
