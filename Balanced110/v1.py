#! /usr/bin/env python
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
class Solution:
  # @param {TreeNode} root
  # @return {boolean}
  def isBalanced(self, root):
    if root == None:
      return True
    if self.getDepth(root.left) > self.getDepth(root.right):
      diff = self.getDepth(root.left) - self.getDepth(root.right)
    else:
      diff = self.getDepth(root.right) - self.getDepth(root.left)
    return (diff <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)
  def getDepth(self, root):
    nodes = [root]
    childs = []
    depth = 0
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
