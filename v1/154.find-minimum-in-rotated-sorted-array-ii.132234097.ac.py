#
# [154] Find Minimum in Rotated Sorted Array II
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (37.77%)
# Total Accepted:    92.6K
# Total Submissions: 245.2K
# Testcase Example:  '[1]'
#
# 
# Follow up for "Find Minimum in Rotated Sorted Array":
# What if duplicates are allowed?
# 
# Would this affect the run-time complexity? How and why?
# 
# 
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# Find the minimum element.
# 
# The array may contain duplicates.
#
class Solution(object):
    def findMin(self, nums):   # 1 star
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return nums[0]
        index = 0
        while index < length - 1:
            if nums[index] > nums[index + 1]:
                return nums[index + 1]
            index += 1
        return nums[0]

        
