single thread numpy implementation
This program calculates all primes in the first n natural numbers,
based on that all primes greater than 3 are either 6k-1 or 6k+1 (k>0).
It requires an approximated total of ((n/3)/(n/log(n)))*(n/log(n))*(n/log(n) + 1)/2 modulo operations,
where ((n/3)/(n/log(n))) is the ratio of candidates checked for primality to the actual number of primes,
and (n/log(n)))*(n/log(n))*(n/log(n) + 1)/2 is the modulo operations required to check all the primes in ascending order,
which makes this method asymptotically slower than O(n) sieve of eratosthenes implementations

interactive usage: python3 interactive.py
usage: python3 interactive.py <n>

numpy_primes.py can also be imported as a module

author: Perry Deng pxdeng@pm.me
date: 02.15.19
