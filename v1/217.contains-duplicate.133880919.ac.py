#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (46.89%)
# Total Accepted:    202.7K
# Total Submissions: 432.3K
# Testcase Example:  '[]'
#
# 
# Given an array of integers, find if the array contains any duplicates. Your
# function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.
# 
#
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 2 star, 运用集合去重，然后比较长度
        length = len(nums)
        _len = len(list(set(nums)))
        return False if length == _len else True
        
