#!/usr/bin/env python

def sumall(*nums):
    print nums
    ret = 0
    for i in range(len(nums)):
        ret += nums[i]
    return ret

a=(1, 2, 3)
print sumall(*a)

