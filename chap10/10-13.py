#!/usr/bin/env python

import bisect

def in_dict(my_dict, word):
    return my_dict[bisect.bisect_right(my_dict, word) - 1] == word

def split_bilocked(word):
    delimiter = ''
    list_word1 = []
    list_word2 = []
    for i in range(len(word)):
        if i % 2 == 0:
            list_word1.append(word[i])
        else:
            list_word2.append(word[i])
    return [delimiter.join(list_word1), delimiter.join(list_word2)]

def is_bilocked(word_list, word, split_words):
    return len(split_words) == 2 and in_dict(word_list, split_words[0]) and in_dict(word_list, split_words[1])

word_list = []
list_file = open('../data/words.txt')
for word in list_file:
    word_list.append(word.strip())

for word in word_list:
    bi_split = split_bilocked(word)
    #print bi_split, ' ', word
    if is_bilocked(word_list, word, bi_split):
        print word, ' ', bi_split[0], ' ', bi_split[1]


