#!/usr/bin/env python

def acc_sum(num_list):
    ret = []
    prev = 0
    for i in range(len(num_list)):
        prev += num_list[i]
        ret.append(prev)
    return ret

print(acc_sum([1, 2, 3]))


