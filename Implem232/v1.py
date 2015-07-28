#! /usr/bin/env python
class Queue:
  # initialize your data structure here.
  def __init__(self):
    self.L = []
    self.length = 0

  # @param x, an integer
  # @return nothing
  def push(self, x):
    self.L.append(x)
    self.length += 1

  # @return nothing
  def pop(self):
    self.L.pop(0)
    self.length -= 1

  # @return an integer
  def peek(self):
    return self.L[0]

  # @return an boolean
  def empty(self):
    if self.length == 0:
      return True
    else:
      return False
