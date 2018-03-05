#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (36.48%)
# Total Accepted:    131.8K
# Total Submissions: 361.2K
# Testcase Example:  '[[0]]'
#
# 
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in place.
# 
# 
# click to show follow up.
# 
# Follow up:
# 
# 
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
# 
# 
#
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 4 star.
        column_num = len(matrix)
        row_num = len(matrix[0])
        col = [0 for _ in range(column_num)]
        row = [0 for _ in range(row_num)]
        for i in range(column_num):
            for j in range(row_num):
                if matrix[i][j] == 0:
                    col[i], row[j] = 1, 1
        
        for i in range(column_num):
            for j in range(row_num):
                if col[i] or row[j]:
                    matrix[i][j] = 0
                    
