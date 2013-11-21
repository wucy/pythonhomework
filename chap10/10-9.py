#!/usr/bin/env python

def remove_duplicates(alist):
    now = []
    for e in alist:
        if not (e in now):
            now.append(e)
    return now

a = [1, 2, 1, 3, 1, 4, 5, 6, 7, 7, 8 ,1]
print a
print remove_duplicates(a)
