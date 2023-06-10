#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

test_list = [22, 33, 44, 55]
idx = 2
print("list = {}".format(idx, replace_in_list(test_list, idx, 8)))
