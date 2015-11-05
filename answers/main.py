def fib():

    data = {}

    def helper(n):

        if n == 1: return 1
        if n == 2: return 1

        if n not in data:
            data[n-2] = helper(n-2)
            data[n-1] = helper(n-1)
            data[n] = data[n-2] + data[n-1]

        return data[n]

    return helper

print fib()(100)
