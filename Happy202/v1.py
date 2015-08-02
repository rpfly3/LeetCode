#! /usr/bin/env python
class Solution:
  # @param {integer} n
  # @return {boolean}
  def isHappy(self, n):
    nSet() = set()
    while True:
      Sum = 0
      while n// 10 > 0:
        i = n % 10
        Sum += i * i
        n = n // 10
      Sum += n * n
      if Sum == 1:
        return True
      if Sum in nSet:
        return False
      else:
        nSet.add(Sum)
      n = Sum
# Note that don't forget to check the circle condition:
# when entering a circle, it is impossible to be a 
# happy number!
