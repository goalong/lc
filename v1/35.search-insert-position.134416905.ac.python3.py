#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (40.04%)
# Total Accepted:    237.6K
# Total Submissions: 593.4K
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
# 
# You may assume no duplicates in the array.
# 
# Example 1:
# 
# Input: [1,3,5,6], 5
# Output: 2
# 
# 
# 
# Example 2:
# 
# Input: [1,3,5,6], 2
# Output: 1
# 
# 
# 
# Example 3:
# 
# Input: [1,3,5,6], 7
# Output: 4
# 
# 
# 
# Example 1:
# 
# Input: [1,3,5,6], 0
# Output: 0
# 
# 
#
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 2 star.
        if not nums:
            return 0
        elif target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            for i, num in enumerate(nums):
                if num == target:
                    return i
                if i < len(nums) -1 and nums[i] < target and nums[i+1] > target:
                    return i + 1
                
