#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (38.02%)
# Total Accepted:    139.9K
# Total Submissions: 368K
# Testcase Example:  '[1,2,2]'
#
# 
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# 
# For example,
# If nums = [1,2,2], a solution is:
# 
# 
# 
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rs = []
        nums.sort()
        self.dfs([], 0, nums, rs)
        return rs

    def dfs(self, path, start, nums, rs):
        if len(path) <= len(nums) and path not in rs:
            rs.append(path)
            # return
        for i in range(start, len(nums)):
            self.dfs(path + [nums[i]], i+1, nums, rs)

