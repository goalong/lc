#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (27.97%)
# Total Accepted:    167.3K
# Total Submissions: 598.2K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 
# Given a 2D board and a word, find if the word exists in the grid.
# 
# 
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# 
# 
# For example,
# Given board = 
# 
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# 
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.
# 
#
class Solution:
    def exist(self, board, word):
        # 6 star, must master.
        def dfs(x, y, word):
            if not word:
                return True
            if x > 0 and board[x-1][y] == word[0]:   # up
                temp = board[x][y]
                board[x][y] = "#"
                if dfs(x-1,y, word[1:]):
                    return True
                board[x][y] = temp
            if x < len(board) - 1 and board[x+1][y] == word[0]:
                temp = board[x][y]
                board[x][y] = "#"
                if dfs(x + 1, y, word[1:]):
                    return True
                board[x][y] = temp
            if y > 0 and board[x][y-1] == word[0]:
                temp = board[x][y]
                board[x][y] = "#"
                if dfs(x, y-1, word[1:]):
                    return True
                board[x][y] = temp
            if y < len(board[0]) - 1 and board[x][y+1] == word[0]:
                temp = board[x][y]
                board[x][y] = "#"
                if dfs(x, y + 1, word[1:]):
                    return True
                board[x][y] = temp
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i,j, word[1:]):
                        return True
        return False
