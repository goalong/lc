#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (30.18%)
# Total Accepted:    83K
# Total Submissions: 274.9K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
# 
# 
# For example, given the following matrix:
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# Return 4.
# 
# 
# Credits:Special thanks to @Freezen for adding this problem and creating all
# test cases.
#
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 5 star, idea: http://bookshadow.com/weblog/2015/06/03/leetcode-maximal-square/
        # dp[x][y]表示（x,y)向左以及向上所能组成的最大正方形的变长
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        width = 0
        for x in range(m):
            for y in range(n):
                dp[x][y] = int(matrix[x][y])
                if dp[x][y] and x > 0 and y > 0:
                    dp[x][y] = min(dp[x-1][y], dp[x-1][y-1], dp[x][y-1]) + 1
                width = max(width, dp[x][y])
        return width * width
                    
        
