#!/usr/bin/env python

def has_no_e(word):
    if not ('e' in word):
        return True
    return False

tot = 0
tar = 0

fin = open('../resource/words.txt')

for line in fin:
    word = line.strip()
    if has_no_e(word):
        print word
        tar += 1
    tot += 1

print 'rate=', float(tar) / tot

