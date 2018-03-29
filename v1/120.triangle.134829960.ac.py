#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (34.75%)
# Total Accepted:    127.3K
# Total Submissions: 366.3K
# Testcase Example:  '[[-10]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
# 
# 
# For example, given the following triangle
# 
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
# 
# 
# 
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# 
# 
# 
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
# 
#
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # 6 star, no idea.
        # 求最小值，首先考虑动态规划， 从底部到顶部分别遍历每一层， 每一层索引为j的dp[j]代表从triangle[i][j]到底部路径的和的最小值
        n = len(triangle)
        dp = triangle[-1]
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]

        
