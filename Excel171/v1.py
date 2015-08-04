#! /usr/bin/env python
class Solution:
  # @param {string} s
  # @return {integer}
  def titleToNumber(self, s):
    col = 0
    # string is a good way to loop through non-number set
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    i = 1
    cdict = dict()
    for ch in characters:
      cdict[ch] = i
      i += 1

    for c in s:
      if c in characters:
        col = col * 26 + cdict[c]
    return col
