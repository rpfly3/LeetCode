#! /usr/bin/env python
# Definition for singly-linked list
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  # @param {ListNode} head
  # @param {integer} val
  # @return {ListNode}
  def removeElements(self, head, val):
    while head != None:
      if head.val != val:
        break
      head = head.next

    H = head
    while H != None and H.next != None:
      if H.next.val == val:
        H.next = H.next.next
      else:
        H = H.next
    return head
