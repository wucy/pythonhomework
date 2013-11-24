#!/usr/bin/env python

def invert_dict(hist):
    ret = dict()
    for key in hist:
        ret.setdefault(hist[key], []).append(key)
    return ret

print invert_dict({'a':1, 'b':2, 'c':2})

