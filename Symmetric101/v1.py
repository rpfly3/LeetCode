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
  def isSymmetric(self, root):
    nodes = [root]
    childs = []
    while nodes != []:
      for i in nodes:
        if i != None:
          childs.append(i.left)
          childs.append(i.right)
      nodes = childs[:]
      if len(childs) % 2 != 0:
        return False
      while childs != []:
        left = childs.pop(0)
        right = childs.pop()
        if left != None and right != None:
          if left.val != right.val:
            return False
        elif left != None and right == None:
          return False
        elfi left == None and right != None:
          return False
    return True
