#! /usr/bin/env python
class Solution:
  # @param {integer} n
  # @return {integer} 
  def trailingZeroes(self, n):
    m = 5
    Zeroes = 0
    while n >= m:
      Zeroes += n // m
      m *= 5
    return Zeroes

# The key is counting the number of 5 in the factorials
