#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (24.39%)
# Total Accepted:    371.4K
# Total Submissions: 1.5M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# Input: 123
# Output:  321
# 
# 
# 
# Example 2:
# 
# Input: -123
# Output: -321
# 
# 
# 
# Example 3:
# 
# Input: 120
# Output: 21
# 
# 
# 
# Note:
# Assume we are dealing with an environment which could only hold integers
# within the 32-bit signed integer range. For the purpose of this problem,
# assume that your function returns 0 when the reversed integer overflows.
# 
#
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        pos = True if x > 0 else False
        _s = str(abs(x))[::-1]
        rs = int(_s)
        if rs > 2147483648:
            return 0
        return -rs if not pos else rs
        
