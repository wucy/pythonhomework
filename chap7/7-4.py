#!/usr/bin/env python

def eval_loop():
    while True:
        line = raw_input()
        if line == 'done':
            break
        print eval(line)

eval_loop()
