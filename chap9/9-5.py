#!/usr/bin/env python

def uses_all(word, cand_list):
    for letter in cand_list:
        if not (letter in word):
            return False
    return True

print uses_all('aeiydocpu', 'aeiouzy')

