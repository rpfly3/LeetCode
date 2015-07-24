#! /usr/bin/env python

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

# A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward

class Solution:
  def isPalindrome(self, head):
    # check if the list is empty
    if head == None:
      return True

    # get the length of the list
    Head = head
    length = 0
    while head != None:
      length += 1
      head = head.next

    # divide the list into two parts
    if length % 2 == 0:
      begin2 = length // 2 + 1
    else:
      begin2 = length // 2 + 2

    # get the head of the second half list
    head = Head 
    for i in range(1, begin2-1):
      head = head.next

    # reverse the second half list
    temp1 = None
    temp2 = None
    for i in range(begin2, length):
      temp2 = head.next
      head.next = temp1
      temp1 = head
      head = temp2

    # after the reverse temp1 is the actual head
    head = temp1
    # begin to check palindrome
    H1 = head
    H2 = Head
    Result = True
    for i in range(begin2, length):
      if H1.val == H2.val:
        H1 = H1.next
        H2 = H2.next
      else:
        Result = False
        break

    # correct the order of the second half list
    temp1 = None
    temp2 = None
    for i in range(begin2, length):
      temp2 = head.next
      head.next = temp1
      temp1 = head
      head = temp2

    return Result


