#! /usr/bin/env python
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def getIntersectionNode(self, headA, headB):
    HEADA = headA
    HEADB = headB

    #Get the length of two linked lists
    lengthA = 0
    lengthB = 0
    while headA != None:
      lengthA += 1
      headA = headA.next

    while headB != None:
      lengthB += 1
      headB = headB.next

    headA = HEADA
    headB = HEADB
    #Set the start point
    if lengthA > lengthB:
      while lengthA != lengthB:
        lengthA -= 1
        headA = headA.next
    else:
      while lengthA != lengthB:
        lengthB -= 1
        headB = headB.next

    #Find the intersection
    while headA != None:
      if headA.val == headB.val:
        return headA
      headA = headA.next
      headB = headB.next
    
    return None

# Submission Result: Accepted
# Note that: 1. the common list of the two lists is from the intersection point to the end of them; if they are two doublely linked lists, we can easily find the intersection point, by traversing from the end of them.
