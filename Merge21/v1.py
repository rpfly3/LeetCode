#! /usr/bin/env python
# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
class Solution:
  # @param {ListNode} l1
  # @param {ListNode} l2
  # @return {ListNode}
  def mergeTwoLists(self, l1, l2):
    if l1 == None and l1 == None:
      return None
    if l1 == None and l2 != None:
      return l2
    if l1 != None and l2 == None:
      return l1
    if l1.val < l2.val:
      Head = head = l1
      l1 = l1.next
    else:
      Head = head = l2
      l2 = l2.next

    while l1 != None and l2 != None:
      if l1.val < l2.val:
        head.next = l1
        l1 = l1.next
        head = head.next
      else:
        head.next = l2
        l2 = l2.next
        head = head.next
    if l1 != None:
      head.next = l1
    else:
      head.next = l2
    return Head
