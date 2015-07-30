#! /usr/bin/env python
class Solution:
  # @param {integer[]} nums
  # @param {integer} k
  # @return {boolean}
  def containsNearbyDuplicate(self, nums, k):
    numsDict = dict()
    for i in range(0, len(nums)):
      idx = numsDict.get(nums[i])
      if idx >= 0 and i- idx <= k:
        return True
      # insert new elements and update the index of existing element
      numsDict[nums[i]] = i
    return False

# Note: 1. This problem shows the importance of data structure
#          and that it is more effecient to find element in dict than others#          because dict is a hashtable in python.
#       2. The index of element should be update in time
