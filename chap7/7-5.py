#!/usr/bin/env python

import math

def factorial(n):
    if n == 0:
        return 1
    ret = 1
    for i in range(2, n + 1):
        ret = ret * i
    return ret

def calc_pi():
    tot = 0.0
    term = 100.0;
    k = 0
    while term > 1e-15:
        term = float(factorial(4 * k) * (1103 + 26390 * k)) / (factorial(k) ** 4 * 396 ** (4 * k))
        tot += term
        k = k + 1

    tot = tot * 2 * math.sqrt(2) / 9801

    return 1 / tot


print calc_pi()


