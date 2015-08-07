#! /usr/bin/env python
class Solution:
  # @param {string[]} strs
  # @return {string}
  def longestCommonPrefix(self, strs):
    common = ''
    if strs == []:
      return common
    for j in range(len(strs[0])):
      for i in range(1, len(strs)):
        if len(strs[i]) < j+1 or strs[i][j] != strs[0][j]:
          return common
      common = common + strs[0][j]
    return common
