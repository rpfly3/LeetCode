#! /usr/bin/env python
class Solution:
  # @param n, an integer
  # @return an integer
  def hammingWeight(self, n):
    div = 1
    count = 0
    while n // div >= 1:
      div *= 2
    while n > 0:
      if n // div == 1:
        n -= div
        count += 1
      div = div // 2
    return count
