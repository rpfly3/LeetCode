#! /usr/bin/env python

#Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  # @param {ListNode} head
  # @return {ListNode}
  def reverseList(self, head):
    temp1 = None
    while head != None:
      temp2 = head.next
      head.next = temp1
      temp1 = head
      head = temp2
    head = temp1

    return head
