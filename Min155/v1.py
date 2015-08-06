#! /usr/bin/env python
class MinStack:
  # initialize your data structure here.
  def __init__(self):
    self.L = []
    self.Min = 0
  # @param x, an integer
  # @return nothing
  def push(self, x):
    self.L.append(x)
    if self.L[self.Min] > x:
      self.Min = len(self.L) - 1

  # @return nothing
  def pop(self):
    if self.Min != len(self.L) -1:
      self.L.pop()
    else:
      self.L.pop()
      self.Min = 0
      for i in range(len(self.L)):
        if self.L[i] < self.L[self.Min]:
          self.Min = i

  # @return an integer
  def top(self):
    return self.L[-1]

  # @return an integer
  def getMin(self):
    return self.L[self.Min]
