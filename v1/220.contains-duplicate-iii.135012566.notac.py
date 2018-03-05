#
# [220] Contains Duplicate III
#
# https://leetcode.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (18.81%)
# Total Accepted:    65K
# Total Submissions: 345.7K
# Testcase Example:  '[]\n0\n0'
#
# 
# Given an array of integers, find out whether there are two distinct indices i
# and j in the array such that the absolute difference between nums[i] and
# nums[j] is at most t and the absolute difference between i and j is at most
# k.
# 
#
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k == 0:
            return False
        n = len(nums)
        right = 1
        while right < n:
            for left in range(max(0, right-k), right):
                gap = abs(nums[left] - nums[right])
                if gap <= t:
                    return True
            right += 1
        return False

