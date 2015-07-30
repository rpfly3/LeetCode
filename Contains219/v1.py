#! /usr/bin/env python
class Solution:
  # @param {integer[]} nums
  # @param {integer} k
  # @return {boolean}
  def containsNearbyDuplicate(self, nums, k):
    if nums == []:
      return False
    for i in range(0, len(nums)):
      if nums[i] in nums[i+1: i+k+1]:
        return True

    return False

# Result: time exceeding error
