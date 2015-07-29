#! /usr/bin/env python
# Definition for a binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  # @param {TreeNode} root
  # @return {TreeNode}
  def invertTree(self, root):
    # Test if the tree is empty
    if root == None:
      return None

    Temp = root.left
    root.left = root.right
    root.right = Temp

    self.invertTree(root.left)
    self.invertTree(root.right)
    
    return root
