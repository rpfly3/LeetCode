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
  def levelOrderBottom(self, root):
    nodes = [root]
    childs = []
    result = []
    if root == None:
      return result
    result.append([root.val])
    while nodes != []:
      vals = []
      for i in nodes:
        if i.left != None:
          childs.append(i.left)
          vals.append(i.left.val)
        if i.right != None:
          childs.append(i.right)
          vals.append(i.right.val)
      nodes = childs
      childs = []
      if vals != []:
        result.append(vals)
    # most methods return None instead of the object itself
    result.reverse()
    return result
