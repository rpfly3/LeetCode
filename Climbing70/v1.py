#! /usr/bin/env python
class Solution:
  # @param {integer} n
  # @return {integer}
  def climbStairs(self, n):
    ways = []
    for i in range(n//2 + 1):
      way = 1
      div = 1
      for j in range(0, i):
        way *= (n-(i+j))
      for k in range(1, i+1):
        div *= k
      way = way // div
      ways.append(way)
    return sum(ways)
