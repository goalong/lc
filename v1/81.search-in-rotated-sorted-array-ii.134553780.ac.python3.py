#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (32.71%)
# Total Accepted:    114.8K
# Total Submissions: 350.9K
# Testcase Example:  '[]\n5'
#
# 
# Follow up for "Search in Rotated Sorted Array":
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
# Write a function to determine if a given target is in the array.
# 
# The array may contain duplicates.
#
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # 6 star. must master.
        low , high = 0, len(nums) - 1
        while low <= high:
            middle = (low+high)//2
            if nums[middle] == target:
                return True
            if nums[middle] == nums[low] == nums[high]:   # 这个情况没想到
                low += 1
                high -= 1
            elif nums[middle] >= nums[low]:
                if nums[middle] > target and target >= nums[low]:
                    high = middle - 1
                else:
                    low = middle + 1
            elif nums[middle] <= nums[high]:
                if target > nums[middle] and target <= nums[high]:
                    low = middle + 1
                else:
                    high = middle - 1
        return False
