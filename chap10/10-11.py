#!/usr/bin/env python

def bisect(alist, word):
    left = 0
    right = len(alist) - 1
    while left < right:
        now = (left + right) / 2
        #print left, ' ', right, ' ', now, ' ', alist[now], ' ', word
        if alist[now] == word:
            return now
        elif alist[now] > word:
            right = now - 1
        else:
            left = now + 1
    return None

word_list = []
dict_file = open('../data/words.txt')
for e in dict_file:
    word_list.append(e.strip())

print bisect(word_list, 'boy')

import bisect

print bisect.bisect(word_list, 'boy') - 1
