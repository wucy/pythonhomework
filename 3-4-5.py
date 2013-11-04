def do_twice(func, val):
    func(val)
    func(val)

def print_twice(val):
    print val

def do_four(func, val):
    do_twice(func, val)
    do_twice(func, val)

do_four(print_twice, 'spam')
