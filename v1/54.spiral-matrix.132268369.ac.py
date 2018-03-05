#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (27.11%)
# Total Accepted:    134K
# Total Submissions: 494.4K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# 
# 
# For example,
# Given the following matrix:
# 
# 
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 
# 
# You should return [1,2,3,6,9,8,7,4,5].
# 
#
class Solution(object):
    def spiralOrder(self, matrix):  # 3 star, no idea
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rs = []
        while matrix:
            if matrix[0]:
                rs.extend(matrix.pop(0))
            if matrix and matrix[0]:
                for row in matrix:
                    rs.append(row.pop())
            if matrix:
                rs += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    rs.append(row.pop(0))
        return rs
        
