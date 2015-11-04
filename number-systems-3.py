def bin2dec(n, base):

    output = 0          
    nstr = str(n)       
    i=0

    while (i < len(nstr)):

        x = int(nstr[len(nstr)-1 -i])
        output += x * pow(base, i)
        i += 1

    return output

print bin2dec(111011111, 2)
print bin2dec(111011111, 8)
