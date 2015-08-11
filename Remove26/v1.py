#! /usr/bin/env python
class Solution:
  # @param {integer[]} nums
  # @return {integer}
  def removeDuplicates(self, nums):
    i = 0
    while i+1 < len(nums):
      if nums[i] == nums[i+1]:
        nums.pop(i+1)
      else:
        i += 1
    return len(nums)
