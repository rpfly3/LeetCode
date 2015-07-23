#! /usr/bin/env python
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

# The lowest common ancestor is defined between two nodes v and w as the lowest node T that was both v and w as descedents (where we allow a node to be a descendant of itself.

class Solution:
  def lowestCommonAncestor(self, root, p, q):
    # The binary search tree might be empty
    if root == None:
      return None

    if (p.val > root.val and q.val < root.val) or (p.val < root.val and q.val > root.val) or p.val == root.val or q.val == root.val:
      return root

    if p.val < root.val and q.val < root.val:
      return self.lowestCommonAncestor(root.left, p, q)
    
    if q.val > root.val and q.val > root.val:
      return self.lowestCommonAncestor(root.right, p, q)

# Don't forget root, p, and q are all nodes, and they have val attribute.
