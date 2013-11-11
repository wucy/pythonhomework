#!/usr/bin/env python

def rotate_word(word, t):
    word = word.upper()
    base = ord('A')
    new = ''
    for letter in word:
        new += chr((ord(letter) + t - base) % 26 + base)

    return new

print rotate_word('abCdEFGHijklmnopqrStuvWXyZ', 300)

