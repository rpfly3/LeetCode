#! /usr/bin/env python

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

# A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward

class Solution:
  def isPalindrome(self, head):
    if head == None:
      return True
    Head = head
    HEAD = head
    length = 0
    while head != None:
      head = head.next
      length += 1

    if length % 2 == 0:
      length = length / 2
      Length = length / 2
    else:
      length = length // 2 + 1
      Length = length // 2

    head = HEAD
    LENGTH = Length
    while length > 0:
      length -= 1
      head = head.next
    
    while head != None:
      while Length > 0:
        Head = Head.next
        Length -= 1
      if Head.val != head.val:
        return False
      LENGTH -= 1
      Length = LENGTH
      head = head.next
      Head = HEAD

    return True

