#!/usr/bin/env python

fin = open('../resource/words.txt')

for line in fin:
    word = line.strip()
    if len(word) > 20:
        print word


