n = 111011111
output = 0          
nstr = str(n)       
i=0

while (i < len(nstr)):

    x = int(nstr[len(nstr)-1 -i])
    output += x * pow(2, i)
    i += 1

print output        

