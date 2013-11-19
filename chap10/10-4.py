#!/usr/bin/env python

def middle(alist):
    ret = []
    for i in range(len(alist) - 2):
        ret.append(alist[i + 1])

    return ret

alist = [1, 2, 3, 4]
print middle(alist)

