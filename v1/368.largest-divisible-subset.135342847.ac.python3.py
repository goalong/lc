#
# [368] Largest Divisible Subset
#
# https://leetcode.com/problems/largest-divisible-subset/description/
#
# algorithms
# Medium (33.86%)
# Total Accepted:    32.5K
# Total Submissions: 96.1K
# Testcase Example:  '[1,2,3]'
#
# 
# Given a set of distinct positive integers, find the largest subset such that
# every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj %
# Si = 0.
# 
# 
# If there are multiple solutions, return any subset is fine.
# 
# 
# Example 1:
# 
# nums: [1,2,3]
# 
# Result: [1,2] (of course, [1,3] will also be ok)
# 
# 
# 
# Example 2:
# 
# nums: [1,2,4,8]
# 
# Result: [1,2,4,8]
# 
# 
# 
# Credits:Special thanks to @Stomach_ache for adding this problem and creating
# all test cases.
#
class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 6 star, no idea, from: https://www.hrwhisper.me/leetcode-largest-divisible-subset/
        if not nums:
            return []
        nums.sort()
        size = len(nums)
        dp = [1] * size
        pre = [None] * size
        max_index = 0
        max_dp = 1
        for i in range(size):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j]+1 > dp[i]:
                    dp[i] = dp[j] + 1
                    pre[i] = j
                if dp[i] > max_dp:
                    max_dp, max_index = dp[i], i
        rs = []
        while max_index is not None:
            rs.append(nums[max_index])
            max_index = pre[max_index]
        return rs
            
                
        
        
