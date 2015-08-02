#! /usr/bin/env python
class Solution:
  # @param {integer} x
  # @return {integer} 
  def reverse(self, x):
    overFlow = 2**31
    y = 0 
    if x < 0:
      neg = True
      x = -x
    else:
      neg = False
    while x // 10 != 0:
      s = x % 10
      y = y * 10 + s
      x = x // 10
    if neg:
      y = -(y * 10 + x)
      if y < -overFlow:
        return 0
    else:
      y = y * 10 + x
      if y > overFlow:
        return 0
    return y
# Note that x is a signed integer !!!
