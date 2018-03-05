#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (40.81%)
# Total Accepted:    97.2K
# Total Submissions: 238.1K
# Testcase Example:  '0'
#
# Given an integer n, generate a square matrix filled with elements from 1 to
# n2 in spiral order.
# 
# 
# For example,
# Given n = 3,
# 
# You should return the following matrix:
# 
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
# 
#
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # 3 star.
        rs = [[0]*n for _ in range(n)]
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        num = 1
        while left < right and top < bottom:
            for i in range(left, right):
                rs[top][i] = num
                num += 1
            for i in range(top, bottom):
                rs[i][right] = num
                num += 1
            for i in range(right, left, -1):
                rs[bottom][i] = num
                num += 1
            for i in range(bottom, top, -1):
                rs[i][left] = num
                num += 1
            left, right = left + 1, right -1
            top, bottom = top + 1, bottom - 1
        if left == right and top == bottom:
            rs[top][left] = num
        return rs
