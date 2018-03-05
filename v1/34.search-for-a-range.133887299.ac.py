#
# [34] Search for a Range
#
# https://leetcode.com/problems/search-for-a-range/description/
#
# algorithms
# Medium (31.60%)
# Total Accepted:    179.1K
# Total Submissions: 566.7K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers sorted in ascending order, find the starting and
# ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# 
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].
# 
#
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 4 star.
        if not nums:
            return [-1, -1]
        low, high = 0, len(nums) - 1
        left, right = -1, -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                left, right = mid, mid
                for i in range(mid, len(nums)):
                    if nums[i] == target:
                        right = i
                    else:
                        break
                for j in range(mid, -1, -1):
                    if nums[j] == target:
                        left = j
                    else:
                        break
                return [left, right]
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return [left, right]
        
