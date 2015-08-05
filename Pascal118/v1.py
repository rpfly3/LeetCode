#! /usr/bin/env python
class Solution:
  # @param {integer} numRows
  # @param {integer[][]}
  def generate(self, numRows):
    if numRows == 0:
      return []
    results = [[1]]
    if numRows == 1:
      return results
    for i in range(1, numRows):
      res = [1]
      for j in range(1, i):
        res.append(results[i-1][j-1] + results[i-1][j])
      res.append(1)
      results.append(res)

    return results
# It's kind of strange that some elegant codes don't work !!! 
