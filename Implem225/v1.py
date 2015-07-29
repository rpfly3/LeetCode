#! /usr/bin/env python
class Stack:
  # initialize your data structure here
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
    self.L.pop()
    self.length -= 1

  # @return an integer
  def top(self):
    if self.length == 0:
      return None
    else:
      return self.L[-1]

  # @return an boolean
  def empty(self):
    if self.length == 0:
      return True
    else:
      return False

# Note that because there is only one parameter 'self' for each method, when referring the parameters, they should be prefixed with 'self'.
# The reason of maintaining a length is that function/method call is too expensive
