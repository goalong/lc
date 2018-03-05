#
# [167] Two Sum II - Input array is sorted
#
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Easy (47.30%)
# Total Accepted:    126K
# Total Submissions: 266.4K
# Testcase Example:  '[2,3,4]\n6'
#
# Given an array of integers that is already sorted in ascending order, find
# two numbers such that they add up to a specific target number.
# 
# The function twoSum should return indices of the two numbers such that they
# add up to the target, where index1 must be less than index2. Please note that
# your returned answers (both index1 and index2) are not zero-based.
# 
# You may assume that each input would have exactly one solution and you may
# not use the same element twice.
# 
# 
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
# 
#
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        memo = {}
        for index, n in enumerate(numbers):
            if target - n in memo:
                return [memo[target-n], index + 1]
            else:
                memo[n] = index + 1

