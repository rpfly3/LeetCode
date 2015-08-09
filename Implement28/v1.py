#! /usr/bin/env python
class Solution:
  # @param {string} haystack
  # @param {string} needle
  # @return {integer}
  def strStr(self, haystack, needle):
    if haystack == '' and needle != '':
      return -1
    if needle == '':
      return 0
    for i in range(len(haystack)):
      if haystack[i] == needle[0]:
        if i + len(needle) > len(haystack):
          return -1
        for j in range(1, len(needle)):
          if haystack[i+j] != needle[j]:
            break
        else:
          return i
    return -1
