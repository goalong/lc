#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (32.11%)
# Total Accepted:    128.7K
# Total Submissions: 400.9K
# Testcase Example:  '[[0]]'
#
# Follow up for "Unique Paths":
# 
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
# 
# [
# ⁠ [0,0,0],
# ⁠ [0,1,0],
# ⁠ [0,0,0]
# ]
# 
# The total number of unique paths is 2.
# 
# Note: m and n will be at most 100.
#
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
         
        # base case
        dp = [[0 for j in xrange(cols)] for i in xrange(rows)]
        for i in xrange(cols):
            if obstacleGrid[0][i] == 0: dp[0][i] = 1
            else: break
        for i in xrange(rows):
            if obstacleGrid[i][0] == 0: dp[i][0] = 1
            else: break
         
        # dynamic programming
        for i in xrange(1, rows):
            for j in xrange(1, cols):
                dp[i][j] = 0 if obstacleGrid[i][j] == 1 else dp[i - 1][j] + dp[i][j - 1]
        return dp[rows - 1][cols - 1]
