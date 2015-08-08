#! /usr/bin/env python
# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
class Solution:
  # @param {ListNode} head
  # @return {ListNode}
  def deleteDuplicates(self, head):
    indicator = head
    while indicator != None:
      while indicator.next != None and indicator.val == indicator.next.val:
        indicator.next = indicator.next.next
      indicator = indicator.next
    return head
