#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (41.81%)
# Total Accepted:    144.4K
# Total Submissions: 345.4K
# Testcase Example:  '1'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1...n?
# 
# 
# For example,
# Given n = 3, there are a total of 5 unique BST's.
# 
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
#
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 6 star， 没有理解
        # 求数量，一般考虑动态规划，dp[0], dp[1], dp[2] = 1, 1, 2, 对于n>2, dp[n] = dp[0]*dp[n-1] +dp[1]*dp[[n-2] + ..+dp[n-1]*dp[0]
        dp = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            s = 0
            for j in range(i):
                s += dp[j] * dp[i - 1 - j]
            dp[i] = s
        return dp[-1]

