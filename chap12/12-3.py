#!/usr/bin/env python

def most_frequent(word):
    word = word.lower()
    freq_dict = dict()
    for letter in word:
       freq_dict[letter] = freq_dict.get(letter, 0) + 1
    sort_list = []
    for key in freq_dict:
        sort_list.append((freq_dict[key], key))
    sort_list.sort(reverse=True)
    ret = []
    for e in sort_list:
        ret.append(e[1])
    return ret

print most_frequent('iamaxiaoxiaoniao')

