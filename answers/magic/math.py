def fib(n):

    if n == 1: return 1
    if n == 2: return 1
    return fib(n-1) + fib(n-2)

def fiba(n):

    a, b = 1, 1

    for i in range(n-1):
        a, b = b, a + b

    return a

def sums(*n):
    retval = 0
    for i in n: retval += i
    return retval
