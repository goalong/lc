#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (34.57%)
# Total Accepted:    72.1K
# Total Submissions: 208.6K
# Testcase Example:  '[]'
#
# Note: This is an extension of House Robber.
# 
# After robbing those houses on that street, the thief has found himself a new
# place for his thievery so that he will not get too much attention. This time,
# all houses at this place are arranged in a circle. That means the first house
# is the neighbor of the last one. Meanwhile, the security system for these
# houses remain the same as for those in the previous street. 
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Credits:Special thanks to @Freezen for adding this problem and creating all
# test cases.
#
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 5 star, no idea. 分两种情况，抢第一家和不抢第一家
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self._rob(nums[1:]), self._rob(nums[:-1]))

    
    def _rob(self, nums):
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        return dp[-1]
        
