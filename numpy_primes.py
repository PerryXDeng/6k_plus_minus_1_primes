"""
super fast single thread numpy implementation
calculates all primes in the first n natural numbers
based on that all primes greater than 3 are either 2k-1 or 2k+1 (k>0)
author: Perry Deng pxdeng@pm.me
date: 02.15.19
"""

import numpy as np
import math


def calculate_primes(n):
  """
  calculates all primes in the first n natural numbers
  based on that all primes greater than 3 are either 2k-1 or 2k+1 (k>0),
  that square roots of primes cannot be factored by primes smaller than themselves,
  and that the number of primes in the first n integers can be approximated by
  n / ln(n)
  :param n: first n natural numbers
  :return: numpy array of primes in first n natural numbers
  """
  largest = (n - 1) // 6 # number of possible values of 2k +- 1 up to n
  temp = (np.arange(1, largest + 1, dtype=np.uint32)) * 6 # [1, 2, ..., largest]
  candidates =np.empty((largest, 2), dtype=np.uint32)
  candidates[:, 0] = temp - 1
  candidates[:, 1] = temp + 1
  candidates = candidates.flatten() # all values of 2k +- 1 up to n
  total_candidates = candidates.shape[0]
  prime_theorem_divisor = math.log(n) / 1.25
  primes = np.empty(int(n // prime_theorem_divisor), dtype=np.uint32)
  primes[0] = 2
  primes[1] = 3
  num_primes = 2
  up_to = 0
  for i in range(total_candidates):
    candidate = candidates[i]
    while primes[up_to] < math.sqrt(candidate):
      up_to += 1
    remainders = np.mod(candidate, primes[0:up_to + 1])
    prime = np.all(remainders) # true if does not contain 0
    if prime:
      primes[num_primes] = candidate
      num_primes += 1
  return primes[0:num_primes]
