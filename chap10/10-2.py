#!/usr/bin/env python

def capitalize_all(nested_list):
    ret = []
    for e in nested_list:
        sub = []
        for x in e:
            sub.append(x.capitalize())
        ret.append(sub)
    return ret

nlist = [['a', 'b'], ['c']]

print capitalize_all(nlist)
print nlist

