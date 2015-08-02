#! /usr/bin/env python

class Solution:
  # @param {integer} n
  # @param {integer}
  def countPrimes(self, n):
    # this is a good way to initialize list
    isPrime = [True] * max(n, 2)
    isPrime[0] = False
    isPrime[1] = False
    i = 2
    while i * i < n:
      # the Sieve of Eratothenes algorithm
      if isPrime[i]:
        j = i * i
        while j < n:
          isPrime[j] = False
          j += i
      i += 1
    # the sum() function
    return sum(isPrime)
# The time limit is too strict for python
