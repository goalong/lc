#
# [26] Remove Duplicates from Sorted Array
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
#
# algorithms
# Easy (36.14%)
# Total Accepted:    325.9K
# Total Submissions: 901.7K
# Testcase Example:  '[1,1,2]'
#
# 
# Given a sorted array, remove the duplicates in-place such that each element
# appear only once and return the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# 
# 
# Example:
# 
# Given nums = [1,1,2],
# 
# Your function should return length = 2, with the first two elements of nums
# being 1 and 2 respectively.
# It doesn't matter what you leave beyond the new length.
# 
# 
#
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 4 star.
        if not nums:
            return 0
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != nums[j]:
                nums[j+1], nums[i] = nums[i], nums[j+1]
                j += 1
        return j+1
        
