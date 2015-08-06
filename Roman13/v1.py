#! /usr/bin/env python
class Solution:
  # @param {string} s
  # @param {integer}
  def romanToInt(self, s):
    rdict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    if s == '':
      return result
    s = s.upper()
    s = s[::-1]
    last = None
    for x in s:
      if last and rdict[x] < last:
        # There is at most one letter less than than the current one !!!
        result = result -2*rdict[x]
      result = result + rdict[x]
      last = rdict[x]
    return result
