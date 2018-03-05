#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (50.24%)
# Total Accepted:    139.9K
# Total Submissions: 278.5K
# Testcase Example:  '[0,0]'
#
# 
# Given an array of n integers where n > 1, nums, return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
# 
# Solve it without division and in O(n).
# 
# For example, given [1,2,3,4], return [24,12,8,6].
# 
# Follow up:
# Could you solve it with constant space complexity? (Note: The output array
# does not count as extra space for the purpose of space complexity analysis.)
#
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 4 star. no idea.
        n = len(nums)
        rs = [1] * n
        left = 1
        for i in range(n-1):
            left *= nums[i]
            rs[i+1] *= left
        right = 1
        for j in range(n-1, 0, -1):
            right *= nums[j]
            rs[j-1] *= right
        return rs
        
