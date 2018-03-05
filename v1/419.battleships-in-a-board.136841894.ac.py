#
# [419] Battleships in a Board
#
# https://leetcode.com/problems/battleships-in-a-board/description/
#
# algorithms
# Medium (62.93%)
# Total Accepted:    40K
# Total Submissions: 63.6K
# Testcase Example:  '[["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]'
#
# Given an 2D board, count how many battleships are in it. The battleships are
# represented with 'X's, empty slots are represented with '.'s. You may assume
# the following rules:
# 
# 
# You receive a valid board, made of only battleships or empty slots.
# Battleships can only be placed horizontally or vertically. In other words,
# they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1
# column), where N can be of any size.
# At least one horizontal or vertical cell separates between two battleships -
# there are no adjacent battleships.
# 
# 
# Example:
# X..X
# ...X
# ...X
# 
# In the above board there are 2 battleships.
# 
# Invalid Example:
# ...X
# XXXX
# ...X
# 
# This is an invalid board that you will not receive - as battleships will
# always have a cell separating between them.
# 
# Follow up:Could you do it in one-pass, using only O(1) extra memory and
# without modifying the value of the board?
#
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        # 5 star, no idea, http://bookshadow.com/weblog/2016/10/13/leetcode-battleships-in-a-board/
        h = len(board)
        w = len(board[0]) if h else 0

        ans = 0
        for x in range(h):
            for y in range(w):
                if board[x][y] == 'X':
                    if x > 0 and board[x - 1][y] == 'X':
                        continue
                    if y > 0 and board[x][y - 1] == 'X':
                        continue
                    ans += 1
        return ans
