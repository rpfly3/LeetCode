#! /usr/bin/env python
class Solution:
  # @param {integer[]} nums
  # @return {integer}
  def majorityElement(self, nums):
    majority = None
    count = 0
    for element in nums:
      if count == 0:
        majority = element
        count = 1
      elif majority == element:
        count += 1
      else:
        count -= 1
    return majority
# This algorithm is Moor's Voting Algorithm
# It is applicable only if the majority element appears more than n/2
