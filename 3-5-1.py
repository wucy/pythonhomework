def line(char1, char2):
    print char1, char2 * 4, char1, char2 * 4, char1

def line1():
    line('+', '-')

def line2():
    line('|', ' ')

def do_four(func):
    func()
    func()
    func()
    func()

line1()
do_four(line2)
line1()
do_four(line2)
line1()

