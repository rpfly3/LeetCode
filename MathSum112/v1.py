class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  def hasPathSum(self, root, sum):
    left = False
    right = False

    # Note that the tree might be empty
    if root != None:
      SUM = root.val
    else:
      return False

    if root.left == None and root.right == None:
      if SUM != sum:
        return False
      else:
        return True

    # Note that the sum might be negative
    if root.left != None:
      left = self.hasPathSum(root.left, sum - SUM)
    if root.right != None:
      right = self.hasPathSum(root.right, sum - SUM)

    return left or right

# Note that for trees, the recursion might be the first option
