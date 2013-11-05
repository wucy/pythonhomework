#/usr/bin/env python

from swampy.TurtleWorld import *

def koch(t, length):
    if length < 10.0:
        fd(t, length)
        return
    koch(t, length / 3.0)
    lt(t, 60)
    koch(t, length / 3.0)
    rt(t, 120)
    koch(t, length / 3.0)
    lt(t, 60)
    koch(t, length / 3.0)


def snow(t, length):
    koch(t, length)
    rt(t, 120)
    koch(t, length)
    rt(t, 120)
    koch(t, length)
    rt(t, 120)

world = TurtleWorld()
bob = Turtle()

bob.delay = 0.01

snow(bob, 100)

wait_for_user()
