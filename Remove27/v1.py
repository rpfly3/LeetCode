#! /usr/bin/env python
class Solution:
  # @param {integer[]} nums
  # @param {integer} val
  # @return {integer}
  def removeElement(self, nums, val):
    i = 0
    # Here is one place where the iterator doesn't work
    # See http://stackoverflow.com/questions/1637807/modifying-list-while-iterating
    # for more explanation !!!
    while i < len(nums):
      if nums[i] == val:
        nums.pop(i)
      else:
        i += 1
    return len(nums)
