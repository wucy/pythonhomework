#!/usr/bin/env python

def is_abecedarian(word):
    now = 0
    word = word.upper()
    while now < len(word) - 1:
        if ord(word[now]) > ord(word[now + 1]):
            return False
        now += 1
    return True

print is_abecedarian('abcd')

