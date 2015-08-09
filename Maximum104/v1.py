#! /usr/bin/env python
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
class Solution:
  # @param {TreeNode} root
  # @return {integer}
  def maxDepth(self, root):
    depth = 0
    nodes = [root]
    childs = []
    if root == None:
      return depth
    while nodes != []:
      depth += 1
      for i in nodes:
        if i.left != None:
          childs.append(i.left)
        if i.right != None:
          childs.append(i.right)
      nodes = childs
      childs = []
    return depth
