n = 73
output = ""

while n > 0:

    n, remainder = divmod(n, 2)

    # Prepend the remainder
    output = str(remainder) + output

print int(output)
