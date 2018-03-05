#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (40.29%)
# Total Accepted:    140.6K
# Total Submissions: 349K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# Example 1:
# 
# [[1,3,1],
# ⁠[1,5,1],
# ⁠[4,2,1]]
# 
# Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the
# sum.
# 
#
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
         
        # initialization
        dp = [[0 for j in xrange(cols)] for i in xrange(rows)]
        dp[0][0] = grid[0][0]
        for i in xrange(1, cols):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for i in xrange(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
         
        # dynamic programming
        for i in xrange(1, rows):
            for j in xrange(1, cols):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[rows - 1][cols - 1]
