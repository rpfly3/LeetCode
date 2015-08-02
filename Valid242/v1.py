#! /usr/bin/env python
class Solution:
  # @param {string} s
  # @param {string} t
  # @return {boolean}
  def isAnagram(self, s, t):
    sdict = dict()
    tdict = dict()

    for i in s:
      sdict[i] = sdict.get(i, 0) + 1
    for i in t:
      tdict[i] = tdict.get(i, 0) + 1
    # There might be some character in s not in t, vice versa, so check them both
    for i in sorted(sdict):
      if sdict.get(i, 0) != tdict.get(i, 0):
        return False
    for i in sorted(tdict):
      if sdict.get(i, 0) != tdict.get(i, 0):
        return False

    return True

# An anagram is a word or phrase spelled by rearranging the letters of another word or phrase.
