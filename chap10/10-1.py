#!/usr/bin/env python

def nested_sum(nested_list):
    ret = 0
    for e in nested_list:
        ret += sum(e)
    return ret


list = [[1, 2, 3, 4], [4, 1, 3], [9, 10, 1.23]]
print nested_sum(list)

