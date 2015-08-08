#! /usr/bin/env python
class Solution:
  # @param {integer[]} digits
  # @return {integer[]}
  plus = True
  # range(i, j, k) start from i and plus k, until reach j
  for i in range(len(digits)-1, -1, -1):
    if plus:
      digits[i] += 1
    if digits[i] == 10:
      plus = True
      digits[i] = 0
    else:
      plus = False
  if plus:
    # list.insert(i, x) will insert x before the position i
    digits.insert(0, 1)
  return digits
