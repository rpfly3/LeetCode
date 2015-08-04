#! /usr/bin/env python
class Solution:
  # @param {string} str
  # @return {integer}
  def myAtoi(self, str):
    str = str.strip()
    symSet = {'-', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    if str = '':
      return 0
    if str[0] not in symSet:
      return 0
    output = str[0]
    # range() might be an empty iterator, thus the i used in for loop
    # might be unassigned before using it
    for i in range(1, len(str)):
      if str[i].isdigit():
        output = output + str[i]
      else:
        break
    if output in ('+', '-'):
      return 0
    elif -2147483648 <= int(output) <= 2147483647:
      return int(output)
    elif int(output) > 2147483647:
      return 2147483647
    else:
      return -2147483648
# Note that don't always consider to use less space, especially when it 
# can make things complicated.
