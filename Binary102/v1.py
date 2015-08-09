#! /usr/bin/env python
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
class Solution:
  # @param {TreeNode} root
  # @return {integer[][]}
  def levelOrder(self, root):
    nodes = [root]
    childs = []
    result = []
    if root = None:
      return result
    while nodes != []:
      vals = []
      for i in nodes:
        vals.append(i.val)
        if i.left != None:
          childs.append(i.left)
        if i.right != None:
          childs.append(i.right)
      result.append(vals)
      nodes = childs
      childs = []
    return result
