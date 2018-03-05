#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (38.91%)
# Total Accepted:    116K
# Total Submissions: 298.2K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
# 
# 
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is
# 4. Note that there may be more than one LIS combination, it is only necessary
# for you to return the length.
# 
# 
# Your algorithm should run in O(n2) complexity.
# 
# 
# Follow up: Could you improve it to O(n log n) time complexity? 
# 
# Credits:Special thanks to @pbrother for adding this problem and creating all
# test cases.
#
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 4 star
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] +1, dp[i])
        return max(dp)
        
