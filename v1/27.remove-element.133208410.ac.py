#
# [27] Remove Element
#
# https://leetcode.com/problems/remove-element/description/
#
# algorithms
# Easy (40.53%)
# Total Accepted:    261.9K
# Total Submissions: 646.3K
# Testcase Example:  '[3,2,2,3]\n3'
#
# Given an array and a value, remove all instances of that value in-place and
# return the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# 
# The order of elements can be changed. It doesn't matter what you leave beyond
# the new length.
# 
# Example:
# 
# 
# Given nums = [3,2,2,3], val = 3,
# 
# Your function should return length = 2, with the first two elements of nums
# being 2.
# 
# 
# 
# 
#
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 3 star.
        if not nums:
            return 0
        j = 0
        index = 0
        while j < len(nums):
            if nums[j] == val:
                pass
            else:
                nums[index] = nums[j]
                index += 1
            j += 1
        return index
