#!/usr/bin/env python

import time

def fib_default(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib_default(n - 1) + fib_default(n - 2)

memo = {0:1, 1:1}

def fib_memo(n):
    if n in memo:
        return memo[n]
    else:
        ret = fib_memo(n - 1) + fib_memo(n - 2)
        memo[n] = ret
        return ret

n = 40

sta = time.time()
fib_default(n)
end = time.time()
print end - sta

sta = time.time()
fib_memo(n)
end = time.time()
print end - sta

