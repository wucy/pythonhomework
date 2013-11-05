from swampy.TurtleWorld import *
from math import pi

def square1(t):
    square2(t, 100)

def square2(t, length):
    polygon(t, length, 4)

def polygon(t, length, n):
    for i in range(n):
        fd(t, length)
        lt(t, 360.0 / n)

def circle(t, r):
    arc(t, r, 360)

def arc(t, r, angle):
    cir = 2 * pi * r;
    n = int(cir * angle / 360)
    length = cir / int(cir)
    for i in range(n):
        fd(t, length)
        lt(t, 360.0 / int(cir))
        

world = TurtleWorld()
bob = Turtle()
print bob

bob.delay = 0.01

#square2(bob, 100)
#square1(bob)
#polygon(bob, 1, 100)
#circle(bob, 50)
arc(bob, angle=90, r=50)



wait_for_user()

