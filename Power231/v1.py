#! /usr/bin/env python
class Solution:
  # @param {integer} n
  # @return {boolean}
  def isPowerOfTwo(self, n):
    if n <= 0:
      return False
    while n > 0:
      if n == 1:
        return True
      if n % 2 != 0:
        return False
      n = n / 2
# Note: only for n > 0 can be the power of two;
# and n = 1 if the final step to check if n is the power of two;
