#! /usr/bin/env python

class Solution:
  # @param {string} s
  # @param {string} t
  # @return {boolean}
  def isIsomorphic(self, s, t):
    sdict = dict()
    tdict = dict()
    for i in range(len(s)):
      p = sdict.get(s[i], '')
      q = tdict.get(t[i], '')
      if p == '' and q == '':
        sdict[s[i]] = t[i]
        tdict[t[i]] = s[i]
      else:
        if (p != '' and sdict[s[i]] != t[i]) or (q != '' and tdict[t[i]] != s[i]):
          return False:

    return True

# Note that this is a one-to-one mapping problem
