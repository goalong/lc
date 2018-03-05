#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (46.88%)
# Total Accepted:    85.1K
# Total Submissions: 181.4K
# Testcase Example:  '3\n7'
#
# 
# Find all possible combinations of k numbers that add up to a number n, given
# that only numbers from 1 to 9 can be used and each combination should be a
# unique set of numbers.
# 
# 
# 
# ⁠Example 1:
# Input:  k = 3,  n = 7
# Output: 
# 
# [[1,2,4]]
# 
# 
# ⁠Example 2:
# Input:  k = 3,  n = 9
# Output: 
# 
# [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
#
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # 5 star, dfs
        rs = []
        self.dfs(k, n, 0, [], rs)
        return rs

    def dfs(self, k, n, start, path, rs):   # 重点是维护了start这个变量，保证了结果是升序的，并且不会重复
        if k == 0 and sum(path) == n:
            rs.append(path)
            return
        if k == 0:
            return
        if sum(path) >= n:
            return
        for i in range(start + 1, 10):
            self.dfs(k-1, n, i, path + [i], rs)
