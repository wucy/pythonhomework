#!/usr/bin/env python

word_list = []
word_file = open('../data/words.txt')
for word in word_file:
    word_list.append(word.strip())

reverse_word_list = []
for word in word_list:
    r_word = []
    for i in range(len(word)):
        r_word.append(word[i - 1])
    delimiter = ''
    reverse_word_list.append(delimiter.join(r_word))

import bisect
for i in range(len(word_list)):
    word = reverse_word_list[i]
    if word_list[bisect.bisect(word_list, word) - 1] == word:
        print word_list[i], ' ', word

