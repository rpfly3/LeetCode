#! /usr/bin/env python
class Solution:
  # @param {character[][]} board
  # @return {boolean}
  def isValidSudoku(self, board):
    for i in range(9):
      tdict = {k: False for k in '123456789'}
      for j in range(9):
        if board[i][j] != '.':
          if tdict[board[i][j]]:
            return False
          else:
            tdict[board[i][j]] = True
    for i in range(9):
      tdict = {k: False for k in '123456789'}
      for j in range(9):
        if board[j][i] != '.':
          if tdict[board[j][i]]:
            return False
          else:
            tdict[board[j][i]] = True
    for m in range(0, 9, 3):
      for n in range(0, 9, 3):
        tdict = {k: False for k in '123456789'}
        for i in range(m, m+3):
          for j in range(n, n+3):
            if board[i][j] != '.':
              if tdict[board[i][j]]:
                return False
              else:
                tdict[board[i][j]] = True
    return True
