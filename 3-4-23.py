def do_twice(func, val):
    func(val)
    func(val)

def print_twice(val):
    print val

do_twice(print_twice, 'spam')
