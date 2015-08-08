#! /usr/bin/env python
class Solution:
  # @param {string} a
  # @param {string} b
  # @return {string}
  def addBinary(self, a, b):
    plus = False
    result = ''
    if len(a) > len(b):
      b = '0'*(len(a) - len(b)) + b
    if len(b) > len(a):
      a = '0'*(len(b) - len(a)) + a
    for i in range(len(a)-1, -1, -1):
      if plus:
        temp = int(a[i]) + int(b[i]) + 1
      else:
        temp = int(a[i]) + int(b[i])
      if temp >=2:
        plus = True
        temp = temp % 2
      else:
        plus = False
      result = str(temp) + result
    if plus:
      result = '1' + result
    return result
