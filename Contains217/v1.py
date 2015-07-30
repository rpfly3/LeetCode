#! /usr/bin/env python
class Solution:
  # @param {integer[]} nums
  # @return {boolean}
  def containsDuplicate(self, nums):
    numsDict = dict()
    for i in range(0, len(nums)):
      idi = numsDict.get(nums[i])
      if idi != None:
        return True
      numsDict[nums[i]] = i
    return False
