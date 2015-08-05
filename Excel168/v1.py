#! /usr/bin/env python
class Solution:
  # @param {integer} n
  # @return {string}
  def convertToTitle(self, n):
    edict = dict()
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for i in range(1, 27):
      edict[i] = characters[i-1]
    while n > 0:
      if n % 26 == 0:
        j = 26
      else:
        j = n % 26
      result = edict[j] + result
      n = (n-1) // 26
    return result
