#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (31.97%)
# Total Accepted:    238.9K
# Total Submissions: 747.1K
# Testcase Example:  '[]\n5'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
#
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 6 star.
        low, high = 0, len(nums) - 1
        while low <= high:
            middle = (low+high)//2
            if nums[middle] == target:
                return middle
            if nums[middle] >= nums[low]:
                if nums[middle] > target >= nums[low]:
                    high = middle - 1
                else:
                    low = middle + 1
            elif nums[middle] < nums[high]:
                if nums[high] >= target > nums[middle]:
                    low = middle + 1
                else:
                    high = middle - 1
        return -1
