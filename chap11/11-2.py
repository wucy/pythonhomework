#!/usr/bin/env python


def histogram(word):
    hist = dict()
    for char in word:
        hist[char] = hist.get(char, 0) + 1
    return hist

print histogram('abracadabra')

