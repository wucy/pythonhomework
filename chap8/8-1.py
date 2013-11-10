#!/usr/bin/env python

def reverse():
    line=raw_input()
    for i in range(len(line)):
        print line[-i - 1]


reverse()
