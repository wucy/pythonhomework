#/usr/bin/env python

def chop(alist):
    del alist[0]
    del alist[len(alist) - 1]


alist = [1, 2, 3, 4]
chop(alist)
print alist

