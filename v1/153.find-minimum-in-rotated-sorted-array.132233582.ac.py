#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (40.73%)
# Total Accepted:    185.6K
# Total Submissions: 455.8K
# Testcase Example:  '[1]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
#
class Solution(object):
    def findMin(self, nums):  # 1 star.
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        index = 0
        while index < length - 1:
            if nums[index] > nums[index + 1]:
                return nums[index + 1]
            index += 1
        return nums[0]
            
        
