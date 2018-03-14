#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (40.98%)
# Total Accepted:    206.8K
# Total Submissions: 504.5K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 
# Given a set of candidate numbers (C) (without duplicates) and a target number
# (T), find all unique combinations in C where the candidate numbers sums to
# T. 
# 
# 
# The same repeated number may be chosen from C unlimited number of times.
# 
# 
# Note:
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# 
# 
# For example, given candidate set [2, 3, 6, 7] and target 7, 
# A solution set is: 
# 
# [
# ⁠ [7],
# ⁠ [2, 2, 3]
# ]
# 
# 
#
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 5 star, dfs
        candidates.sort()
        result = []
        self.dfs(candidates, target, 0, [],  result)
        return result 
        
    def dfs(self, candidates, target, index, path, result):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(index, len(candidates)):
            self.dfs(candidates, target-candidates[i], i, path+[candidates[i]], result)
        
