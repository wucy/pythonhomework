#!/usr/bin/env python

def find(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1


print find('abc', 'a', 0)
