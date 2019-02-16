single thread numpy implementation
calculates all primes in the first n natural numbers
based on that all primes greater than 3 are either 2k-1 or 2k+1 (k>0)
requires an approximated total of (n/3)*(n/log(n))*(n/log(n) + 1)/2 modulo operations,
which makes this method asymptotically slower than O(n) sieve of eratosthenes implementations

interactive usage: python3 interactive.py
usage: python3 interactive.py <n>

numpy_primes.py can also be imported as a module

author: Perry Deng pxdeng@pm.me
date: 02.15.19
