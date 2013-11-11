#!/usr/bin/env python

def avoids(word, ban_set):
    for letter in word:
        if letter in ban_set:
            return False
    return True

print avoids('aaaaabbbbc', '2')

