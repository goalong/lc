#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two/description/
#
# algorithms
# Easy (40.65%)
# Total Accepted:    164.3K
# Total Submissions: 404.2K
# Testcase Example:  '1'
#
# 
# Given an integer, write a function to determine if it is a power of two.
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 3 star
        from math import sqrt
        if n <= 0:
            return False
        while n >= 2:
            if n % 2 == 1:
                return False
            n = n // 2
        return True
        
