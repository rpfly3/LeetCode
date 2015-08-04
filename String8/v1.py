#! /usr/bin/env python
class Solution:
  # @param {string} str
  # @return {integer}
  def myAtoi(self, str):
    INT_MAX = 2147483647
    INT_MIN = - 2147483647
    str = str.strip()
    symSet = {'-', '+', '0', '1', '2', '3', '4', '5', '6','7', '8', '9'}
    if str == '':
      return 0
    if str[0] not in symSet:
      return 0
    i = 1
    while i < len(str):
      if (not str[i].isdigit()):
        break
      i += 1
    if str[0].isdigit():
      if int(str[0:i]) > INT_MAX:
        return INT_MAX
      else:
        return int(str[0:i])
    else:
      if i == 1:
        return 0
      if str[0] is '-':
        if -int(str[1:i]) < INT_MIN:
          return INT_MIN
        else:
          return -int(str[1:i])
      if str[0] is '+':
        if int(str[1:i]) > INT_MAX:
          return INT_MAX
        else:
          return int(str[1:i])
# Result: failed
# Note that: there is no need to design an beautiful program for now !!! 
