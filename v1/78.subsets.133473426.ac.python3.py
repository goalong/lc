#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (44.14%)
# Total Accepted:    220.2K
# Total Submissions: 498.9K
# Testcase Example:  '[1,2,3]'
#
# 
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# 
# For example,
# If nums = [1,2,3], a solution is:
# 
# 
# 
# [
# ⁠ [3],
# ⁠ [1],
# ⁠ [2],
# ⁠ [1,2,3],
# ⁠ [1,3],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 6 star.
        rs = []
        nums.sort()
        self.dfs(0, [], 0, nums, rs)
        return rs

    def dfs(self, count, path, start, nums, rs):
        if count <= len(nums):
            if start > len(nums):
                return
            elif path and start < len(nums) and nums[start] < path[-1]:
                return
            else:
                rs.append(path)
        for i in range(start, len(nums)):
            if i > len(nums) - 1:
                return
            self.dfs(count+1, path+[nums[i]], i+1, nums, rs)
