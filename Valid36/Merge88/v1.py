#! /usr/bin/env python
class Solution:
  # @param {integer[]} nums1
  # @param {integer} m
  # @param {integer[]} nums2
  # @param {integer} n 
  # @return {void} Do not return anything, modify nums1 in-place instead.
  def merge(self, nums1, m, nums2, n):
    i = m-1
    j = n-1
    k = m+n-1
    while i >= 0 and j >= 0:
      if nums2[j] > nums1[i]:
        nums1[k] = nums2[j]
        j -= 1
      else:
        nums1[k] = nums1[i]
        i -= 1
      k -= 1

    while j >= 0:
      nums1[k] = nums[j]
      k -= 1
      j -= 1

# Note that 1. nums1 has been allocated m+n memory
#           2. the number of elements should be based on m and n
