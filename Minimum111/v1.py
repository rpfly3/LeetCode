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
  def minDepth(self, root):
    nodes = [root]
    childs = []
    if root == None:
      return depth
    depth += 1
    while nodes != []:
      for i in nodes:
        if i.left == None and i.right == None:
          return depth
        if i.left != None:
          childs.append(i.left)
        if i.right != None:
          childs.append(i.right)
      nodes = childs
      childs = []
      depth += 1
