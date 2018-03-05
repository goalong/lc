#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (35.07%)
# Total Accepted:    44.2K
# Total Submissions: 126K
# Testcase Example:  '[5,2,6,1]'
#
# 
# You are given an integer array nums and you have to return a new counts
# array.
# The counts array has the property where counts[i] is 
# the number of smaller elements to the right of nums[i].
# 
# 
# Example:
# 
# 
# Given nums = [5, 2, 6, 1]
# 
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# 
# 
# 
# Return the array [2, 1, 1, 0].
# 
#
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        rs = [0] * n
        for i in range(n-2, -1, -1):
            target = None
            for j in range(i+1, n):
               if nums[j] < nums[i]:
                   target = j if not target else target
                   if target != j and nums[j] > nums[target]:
                       target = j
            if not target:
                nums[i] = 0
            else:
                rs[i] = rs[target] + 1
        return rs
