import numpy_primes

"""
an interface for numpy_primes.py
author: Perry Deng pxdeng@pm.me
date: 02.15.19
interactive usage: python3 numpy_primes.py
usage: python3 numpy_primes.py <n>
"""
import sys

def main():
  interactive = False
  if (len(sys.argv) < 2):
    interactive = True
  if interactive:
    n = int(input("I want primes up to: "))
  else:
    n = int(sys.argv[1])
  primes = numpy_primes.calculate_primes(n)
  num = primes.shape[0]
  print("There are " + str(num) + " primes in first " + str(n) + " integers.")
  if interactive:
    to_print = input("Print them all? input y/n\n")
    if to_print == "y":
      for i in primes[0:primes]:
        print(i)

if __name__ == "__main__":
  main()
