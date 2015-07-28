#! /usr/bin/env python
class Solution:
  # @param {integer} x
  # @return {boolean}
  def isPalindrome(self, x):
    if x < 0:
      return False

    div = 1
    while x // div >= 10:
      div *= 10
    while x > 0:
      l = x // div
      r = x % 10
      if l != r:
        return False
      x = x % div // 10
      div = div // 100

    return True

# Note: 1. The base of an integer is 10;
#       2. The difference between extra space and constant space;
#       3. Remember this method to get upper digit of a number;
