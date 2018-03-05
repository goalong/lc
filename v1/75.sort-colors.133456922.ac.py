#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (38.81%)
# Total Accepted:    210.2K
# Total Submissions: 541.6K
# Testcase Example:  '[0]'
#
# 
# Given an array with n objects colored red, white or blue, sort them so that
# objects of the same color are adjacent, with the colors in the order red,
# white and blue.
# 
# 
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
# 
# 
# 
# Note:
# You are not suppose to use the library's sort function for this problem.
# 
# 
# click to show follow up.
# 
# 
# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting
# sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
# array with total number of 0's, then 1's and followed by 2's.
# Could you come up with an one-pass algorithm using only constant space?
# 
# 
#
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 4 star. 计数排序
        count = [0] * 3
        for i in nums:
            count[i] += 1
        index = 0
        for i in range(3):
            for j in range(count[i]):
                nums[index] = i
                index += 1
        
