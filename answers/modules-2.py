import sys
import magic.math

def main():
   print magic.math.sums(int(sys.argv[1]))
   print magic.math.fact(int(sys.argv[1]))

if __name__ == "__main__":
    main()
