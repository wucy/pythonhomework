#!/usr/bin/env python

def is_palindrome(word):
    reverse = word[::-1]
    if word == reverse:
        return True
    return False

print is_palindrome('aaba')
