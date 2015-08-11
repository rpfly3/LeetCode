#! /usr/bin/env python
class Solution:
  # @param {integer} rowIndex
  # @return {integer[]}
  def getRow(self, rowIndex):
    if rowIndex == 0:
      return [1]
    if rowIndex == 1:
      return [1, 1]
    L = [1, 1]
    for i in range(rowIndex-1):
      j = len(L) - 1
      while j > 0:
        L[j] = L[j] + L[j-1]
        j -= 1
      L.append(1)
    return L
