def gcd(a, b):
      while b != 0:
          copyOfB = b
  
          # % is the modulus operator
          b = a % b
          a = copyOfB
  
      return a

print gcd(12,3)
