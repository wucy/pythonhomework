#!/usr/bin/env python

def print_hist(hist):
    keys = hist.keys()
    keys.sort()
    for key in keys:
        print key, ' ', hist[key]


print_hist({'c' : 3, 'a' : 1,'b' : 2})

