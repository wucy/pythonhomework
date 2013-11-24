#!/usr/bin/env python

word_file = open('../data/words.txt')
word_dict = dict()
for word in word_file:
    word_dict[word.strip()] = 1

print word_dict

