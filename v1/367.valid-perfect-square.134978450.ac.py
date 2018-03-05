#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (38.63%)
# Total Accepted:    66.6K
# Total Submissions: 172.3K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# 
# Note: Do not use any built-in library function such as sqrt.
# 
# 
# Example 1:
# 
# Input: 16
# Returns: True
# 
# 
# 
# Example 2:
# 
# Input: 14
# Returns: False
# 
# 
# 
# Credits:Special thanks to @elmirap for adding this problem and creating all
# test cases.
#
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low, high = 0, num
        while low <= high:
            middle = (low+high)//2
            if middle * middle > num:
                high = middle - 1
            elif middle * middle < num:
                low = middle + 1
            else:
                return True
        return False
