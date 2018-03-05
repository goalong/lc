#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (55.27%)
# Total Accepted:    280K
# Total Submissions: 506.7K
# Testcase Example:  '[1]'
#
# Given an array of integers, every element appears twice except for one. Find
# that single one.
# 
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
#
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 4 star, no idea.
        # 一个整数与自己异或的结果是0, 一个整数与0异或的结果是自己, 异或操作满足交换律，即a^b=b^a
        rs = nums[0]
        for i in range(1, len(nums)):
            rs = rs ^ nums[i]
        return rs
        
