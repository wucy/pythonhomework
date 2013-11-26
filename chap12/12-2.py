#!/usr/bin/env python

import random

def unstable_sort(word_list):
    random.seed()
    tri_list = []
    for word in word_list:
        tri_list.append((len(word), random.random(), word))
    tri_list.sort(reverse=True)
    ret = []
    for t in tri_list:
        ret.append(t[2])

    return ret

word_list = []
word_file = open('../data/words.txt')
for word in word_file:
    word_list.append(word.strip())
print unstable_sort(word_list)[0:10]

