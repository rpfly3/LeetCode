#! /usr/bin/env python
# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
class Solution:
  # @param {ListNode} node
  # @return {void} Do not return anything, modify node in-place instead.
  def deleteNode(self, node):
    temp = node.val
    node.val = node.next.val
    node.next.val = temp
    node.next = node.next.next
