#! /usr/bin/env python
class Solution:
  # @param {integer} n
  # @return {string}
  def countAndSay(self, n):
    curStr = '1'
    for i in range(2, n+1):
      count = 0
      preStr = curStr
      curStr = ''
      curCh = preStr[0]
      for ch in preStr:
        if curCh == ch:
          count += 1
        else:
          curStr = curStr + str(count) + curCh
          curCh = ch
          count = 1
      # pay attention to boundary condition when using for loop
      curStr = curStr + str(count) + curCh
    return curStr
