#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

test_list = [22, 33, 44, 55]
idx = -1
print("list[{:d}] = {}".format(idx, element_at(test_list, idx)))
