#! /usr/bin/env python
class Solution:
  # @param {string} s
  # @return {boolean}
  def isValid(self, s):
    stack = []
    sset = {'(', '{', '['}
    for i in s:
      if i in sset:
        stack.append(i)
      elif i == ')':
        if stack != [] and stack[-1] == '(':
          stack.pop()
        else:
          return False
      elif i == ']':
        if stack != [] and stack[-1] == '[':
          stack.pop()
        else:
          return False
      elif i == '}':
        if stack != [] and stack[-1] == '{':
          stack.pop()
        else:
          return False
    if stack != []:
      return False
    else:
      return True
