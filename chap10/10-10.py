#!/usr/bin/env python

def genlist_add(file_name):
    f = open(file_name)
    ret = []
    for line in f:
        ret = ret + [line]
    return ret

def genlist_append(file_name):
    f = open(file_name)
    ret = []
    for line in f:
        ret.append(line)
    return ret

file_name = '../data/words.txt'

import time
sta = time.time()
genlist_add(file_name)
end = time.time()
print 'genlist via add: TIME = ', end - sta


sta = time.time()
genlist_append(file_name)
end = time.time()
print 'genlist via add: TIME = ', end - sta


