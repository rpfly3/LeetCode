#! /usr/bin/env python
# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
class Solution:
  # @param {ListNode} head
  # @param {integer} n
  # @return {ListNode}
  def removeNthFromEnd(self, head, n):
    length = 0
    indicator = head
    while indicator != None:
      length += 1
      indicator = indicator.next
    m = length - n
    # Note that the head might be removed
    if m == 0:
      return head.next
    indicator = head
    i = 1
    while i < m:
      indicator = indicator.next
      i += 1
    indicator.next = indicator.next.next
    return head
