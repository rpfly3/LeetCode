#! /usr/bin/env python
class Solution:
  # @param {integer} A
  # @param {integer} B
  # @param {integer} C
  # @param {integer} D
  # @param {integer} E
  # @param {integer} F
  # @param {integer} G
  # @param {integer} H
  # @return {integer}
  def computeArea{self, A, B, C, D, E, F, G, H):
    l1 = C - A
    w2 = D - B
    s1 = l1 * w1
    l2 = G - E
    w2 = H - F
    s2 = l2 * w2
    S = s1 + s2
    L = [A, C, E, G]
    W = [B, D, F, H]
    L.sort()
    W.sort()
    if C <= E or A >= G:
      return S
    else:
      length = L[2] - L[1]
    if D <= F or B >= H:
      return S
    else:
      width = W[2] - W[1]
    return S - width * length

# Note the in-place sort problem
