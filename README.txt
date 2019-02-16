single thread numpy implementation
This program calculates all primes in the first n natural numbers,
based on that all primes greater than 3 are either 6k-1 or 6k+1 (k>0).
It requires an approximated total of ((n/3)/(n/log(n)))*(n/log(n))*(n/log(n) + 1)/2 modulo operations (if we check for all primes),
where ((n/3)/(n/log(n))) is the ratio of candidates checked for primality to the approximated number of primes,
and (n/log(n)))*(n/log(n))*(n/log(n) + 1)/2 is the modulo operations required to check all the primes in ascending order.
Assuming constant time for modulo operations, the algorithm runs in O(N^2 / logN) time,
which makes this method asymptotically slower than O(n) sieve of eratosthenes implementations

The actual implementation of this algorithm only executes modulo operation for up to the square root value of the candidate, which makes the total number of modulo operations harder to estimate. Empirically the run time of this algorithm T(n) seems to be a linear function with large coefficients. With n = one million, the program takes 4.5 seconds to run on my computer. With n = two million, the program takes 9 seconds to run. With n = ten million, the program takes 45 seconds to run.

interactive usage: python3 interactive.py
usage: python3 interactive.py <n>

numpy_primes.py can also be imported as a module

author: Perry Deng pxdeng@pm.me
date: 02.15.19
