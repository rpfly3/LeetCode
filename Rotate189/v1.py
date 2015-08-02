#! /usr/bin/env python
class Solution:
  # @param {integer[]} nums
  # @param {integer} k
  # @return {void} Do not return anything, modify nums in-place instead.
  def rotate(self, nums, k):
    length = len(nums)
    if length <= 1:
      return
    sdict = dict()
    k = k % length
    for j in range(length):
      if sdict.get(j, 0) == 0:
        p = nums[j-k]
        i = j
        circle = False
        while circle == False:
          q = nums[i]
          nums[i] = p
          p = q
          sdict[i] = 1
          i = (i + k) % length
          if i == j:
            circle = True

# Note that rotation is different from swapping
