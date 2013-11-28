#!/usr/bin/env python

import string
import re


def get_hist_rank_list(raw_word_list):
    ret = []
    hist = dict()
    for word in raw_word_list:
        hist[word] = hist.get(word, 0) + 1
    rank_list = []
    for word in hist:
        rank_list.append((hist[word], word))
    rank_list.sort(reverse=True)
    for e in rank_list:
        ret.append((e[1], e[0]))
    return ret


def get_word_list(file_name):
    ret = []
    word_file = open(file_name)
    for line in word_file:
        line = line.strip().lower()
        for token in string.punctuation:
            line = line.replace(token, ' ')
        for token in string.whitespace:
            line = line.replace(token, ' ')
        for token in {'\xef', '\xbb', '\xbf', '\xc2', '\xca'}:
            line = line.replace(token, ' ')
        line_word_list = re.split(' +', line)
        while '' in line_word_list:
            line_word_list.remove('')
        ret.extend(line_word_list)
    return ret


raw_word_list = get_word_list('../data/pg76.txt')

print get_hist_rank_list(raw_word_list)[:50]

