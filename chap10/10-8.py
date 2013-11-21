#!/usr/bin/env python

def has_duplicates(alist):
    for e in alist:
        cnt = 0
        for f in alist:
            if f == e:
                cnt += 1
        if cnt > 1:
            return True
    return False

print has_duplicates([1, 2, 3, 1])
print has_duplicates([1, 2, 3])


import random

people = []
for i in range(23):
    people.append(random.randint(1, 365))

total = 23 * 22 / 2
got = 0
for i in range(23 - 1):
    for j in range(i + 1, 23):
        if people[i] == people[j]:
            got += 1

print people

print float(got) / total

