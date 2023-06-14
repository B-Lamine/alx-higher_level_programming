#!/usr/bin/python3

def uniq_add(my_list=[]):
    exclude_list = []
    result_sum = 0
    for i in my_list:
        if i not in exclude_list:
            result_sum += i
            exclude_list.append(i)
    return result_sum
