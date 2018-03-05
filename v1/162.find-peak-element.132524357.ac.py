#
# [162] Find Peak Element
#
# https://leetcode.com/problems/find-peak-element/description/
#
# algorithms
# Medium (38.73%)
# Total Accepted:    144.6K
# Total Submissions: 373.3K
# Testcase Example:  '[1,2,3,1]'
#
# A peak element is an element that is greater than its neighbors.
# 
# Given an input array where num[i] ≠ num[i+1], find a peak element and return
# its index.
# 
# The array may contain multiple peaks, in that case return the index to any
# one of the peaks is fine.
# 
# You may imagine that num[-1] = num[n] = -∞.
# 
# For example, in array [1, 2, 3, 1], 3 is a peak element and your function
# should return the index number 2.
# 
# click to show spoilers.
# 
# Note:
# Your solution should be in logarithmic complexity.
# 
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        i = 0
        while i <= n - 1:
            if i == 0:
                if nums[i] > nums[i+1]:
                    return i
            elif i == n-1:
                if nums[i] > nums[i-1]:
                    return i
            else:
                if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                    return i
            i += 1

            
        
