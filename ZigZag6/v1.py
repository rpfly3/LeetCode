#! /usr/bin/env python
class Solution:
  # @param {string} s
  # @param {integer} numRows
  # @return {string}
  def convert(self, s, numRows):
    if numRows <= 1:
      return s
    sdict = dict()
    increase = True
    j = 1
    result = ''
    for i in s:
      sdict[j] = sdict.get(j, '') + i
      if j == 1:
        increase = True
      if j == numRows:
        increase = False
      if increase == True:
        j += 1
      else:
        j -= 1
    for j in range(1, numRows+1):
      result = result + sdict.get(j, '')

    return result

# Note that: the numRows <= 1 is a special case
