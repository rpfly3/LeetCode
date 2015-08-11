#! /usr/bin/env python
class Solution:
  # @param {string} s
  # @return {boolean}
  def isPalindrome(self, s):
    s = s.lower()
    if not s:
      return True
    L = []
    for i in s:
      if i.isalnum():
        L.append(i)
    length = len(L)
    for j in range(length//2):
      if L[j] != L[length-1-j]:
        return False
    return True
