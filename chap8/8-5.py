#!/usr/bin/env python

def count(word, letter):
    now = 0
    cnt = 0
    while now < len(word):
        if word[now] == letter:
            cnt += 1
        now += 1
    return cnt


print count('aaab aa', 'a')

