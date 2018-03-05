#
# [258] Add Digits
#
# https://leetcode.com/problems/add-digits/description/
#
# algorithms
# Easy (51.72%)
# Total Accepted:    189.8K
# Total Submissions: 367K
# Testcase Example:  '0'
#
# 
# Given a non-negative integer num, repeatedly add all its digits until the
# result has only one digit. 
# 
# 
# 
# For example:
# 
# 
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only
# one digit, return it.
# 
# 
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 5 star. no idea.
        if num == 0:
            return 0
        return (num - 1) % 9 + 1
        
