#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (32.80%)
# Total Accepted:    137.1K
# Total Submissions: 418.2K
# Testcase Example:  '[]\n0'
#
# 
# Given an array of integers and an integer k, find out whether there are two
# distinct indices i and j in the array such that nums[i] = nums[j] and the
# absolute difference between i and j is at most k.
# 
#
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 4 star
        n = len(nums)
        gap = n + 1
        memo = {}
        for index, num in enumerate(nums):
            if num in memo:
                gap = min(gap, index - memo[num])
                if gap <= k:
                    return True
                else:
                    memo[num] = index
            else:
                memo[num] = index
        return False
        
