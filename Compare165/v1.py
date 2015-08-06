#! /usr/bin/env python
class Solution:
  # @param {string} version1
  # @param {string} version2
  # @return {integer}
  def compareVersion(self, version1, version2):
    v1List = version1.split('.')
    v2List = version2.split('.')
    v1 = [int(element) for element in v1List]
    v2 = [int(element) for element in v2List]
    if len(v1) > len(v2):
      v2.extend([0]*(len(v1) - len(v2)))
    if len(v1) < len(v2):
      v1.extend([0]*(len(v2) - len(v1)))
    for i in range(len(v1)):
      if v1[i] == v2[i]:
        continue
      elif v1[i] > v2[i]:
        return 1
      else:
        return -1
    return 0
