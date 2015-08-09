#! /usr/bin/env python
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
class Solution:
  # @param {TreeNode} p
  # @param {TreeNode} q
  # @return {boolean}
  def isSameTree(self, p, q):
    if p == None and q == None:
      return True
    elif p == None and q != None:
      return False
    elif p != None and q == None:
      return False
    elif p.val != q.val:
      return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
