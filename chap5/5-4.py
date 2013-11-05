#!/usr/bin/env python

def is_triangle(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        print 'No'
        return
    print 'Yes'

def input_and_check():
    a = float(raw_input('Input a: '))
    b = float(raw_input('Input b: '))
    c = float(raw_input('Input c: '))
    is_triangle(a, b, c)

input_and_check()

