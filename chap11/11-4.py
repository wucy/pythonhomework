#!/usr/bin/env python

def reverse_lookup(dic, val):
    ret = []
    for key in dic:
        if dic[key] == val:
            ret.append(key)
    return ret

print reverse_lookup({'a':1, 'b':2, 'c':2}, 3)

