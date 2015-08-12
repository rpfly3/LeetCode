#! /usr/bin/env python
# Definition for a binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
class BSTIterator:
  # @param root, a binary search tree's root node
  def __init__(self, root):
    self.smallest = []
    self.push(root)

  # @return a boolean, whether we have a next smallest number
  def hasNext(self):
    if self.smallest:
      return True
    else:
      return False

  # @return an integer, the next smallest number
  def next(self):
    top = self.smallest.pop()
    self.push(top.right)
    return top.val

  def push(self, node):
    while node:
      self.smallest.append(node)
      node = node.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


# Note that the BST won't change if you don't change the nodes' relation
# and that if you don't lose the reference to the root of the tree
# then you can traverse the tree still, which means when dealing with 
# tree you should store the root somewhere for future reference. 
