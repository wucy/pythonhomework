def check_fermat(a, b, c, n):
    if n > 2 and a**n + b **n == c**n:
        print 'Fermat is wrong!'
    else:
        print 'Fermat is right!'

def input_and_check():
    a = int(raw_input('Input a: '))
    b = int(raw_input('Input b: '))
    c = int(raw_input('Input c: '))
    n = int(raw_input('Input n: '))
    check_fermat(a, b, c, n)

input_and_check()
