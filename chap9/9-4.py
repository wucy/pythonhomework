#!/usr/bin/env python

def uses_only(word, cand_set):
    word = word.upper()
    cand_set = cand_set.upper()
    for letter in word:
        if not (letter in cand_set):
            return False
    return True


print uses_only('Hoealfalfa', 'acefhlo')

