#!/usr/bin/env python

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    mid = len(word) / 2
    maxid = len(word) - 1
    for i in range(mid):
        if word[maxid - i] != word[i]:
            return False
    return True



print '$', middle('a'), '$'


print is_palindrome('xxx')
