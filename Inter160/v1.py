#!/usr/bin/env python

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
    
class Solution:
  def getIntersection(self, headA, headB):
    HEADA = headA
    HEADB = headB
    while headA != None:
      while headB != None:
        if headA.val == headB.val:
          return headA
        headB = headB.next
      headA = headA.next
      headB = HEADB
    return None
          
# Note that this algorithm is a naive algorithm
# Submission Result: Time Limit Exceeded
