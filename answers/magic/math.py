# Return n*(n-1)*(n-2)*...*1
def fact(n):

    retval = 1

    for i in range(1,n+1):
        retval *= i

    return retval

# Return n+(n-1)+(n-2)+...+1
def sums(n): 

    retval = 0

    for i in range(1,n+1):
        retval += i

    return retval
