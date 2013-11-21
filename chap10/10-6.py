#!/usr/bin/env python

def is_sorted(alist):
    for i in range(len(alist) - 1):
        if alist[i] >= alist[i + 1]:
            return False
    return True


print is_sorted([1, 2, 3, 4, 5])
print is_sorted([2, 1, 3, 4, 5, 6])

