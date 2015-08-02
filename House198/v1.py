#! /usr/bin/env python
class Solution:
  # @param {integer[]} nums
  # @return {integer}
  def rob(self, nums):
    maxSums = [0] * max(len(nums), 2)
    for i in range(len(nums)):
      maxSums[i] = max(maxSums[i-1], maxSums[i-2] + nums[i])
    return maxSums[max(len(nums)-1, 0)]

# Note the most important thing is finding the optimal structure. 
