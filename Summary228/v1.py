#! /usr/bin/env python
class Solution:
  # @param {integer[]} nums
  # @return {string[]}
  def summaryRanges(self, nums):
    result = []
    
    # The nums may be empty
    if len(nums) == 0:
      return result

    beginning = nums[0]
    j = nums[0]
    for i in range(0, len(nums)):
      # First test if there is no continuity
      if nums[i] != j:
        if beginning != j-1:
          result.append(str(beginning)+'->'+str(j-1))
        else:
          result.append(str(beginning))
        # Initialize two variables again
        beginning = nums[i]
        j = nums[i]+1
      else:
        j += 1
      # Then test if reach the end of nums
      if i == len(nums)-1:
        if beginning != nums[i]:
          result.append(str(beginning)+'->'+str(nums[i]))
        else:
          result.append(str(beginning))
    return result

# There are two conditions to terminate the test: uncontinuity and end of nums.
# But uncontinuity should be test first when they happen at the same time.
