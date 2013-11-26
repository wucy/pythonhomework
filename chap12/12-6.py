#!/usr/bin/env python


def is_reducible(word, word_set):
    return word in word_set

word_file = open('../data/words.txt')

word_list = []
for line in word_file:
    word_list.append(line.strip())
word_list.append('a')
word_list.append('i')
word_list.append('')


sort_list = []
for word in word_list:
    sort_list.append((len(word), word))
sort_list.sort()
word_list = []
for t in sort_list:
    word_list.append(t[1])
#print word_list[:10]

reducible_set = set()

ans = ''
reducible_set.add('')

for word in word_list:
    if len(word) == 1:
        reducible_set.add(word)
        ans = word
        continue
    for split_point in range(len(word)):
        left = word[:split_point]
        right = word[split_point + 1:]
        #print left, ' ', right
        if is_reducible(left, reducible_set) and is_reducible(right, reducible_set):
            reducible_set.add(word)
            #print 'left=', left, ' right=', right
            if len(word) > len(ans):
                ans = word

print ans

