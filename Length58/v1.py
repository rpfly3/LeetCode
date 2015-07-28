#! /usr/bin/env python
class Solution:
  # @param {string} s
  # @return {integer}
  def lengthOfLastWord(self, s):
    L = s.split(' ')
    L.reverse()
    for i in range(0, len(L)):
      if len(L[i]) != 0:
        return len(L[i])
    return 0

# Note that reversed() function return a strange object not a sequence
# range(m, n) doesn't include n, from m to n-1
# Another thing is that s.split() will return more empty strings than 
# than expected when there are some continuous empty spaces in s
