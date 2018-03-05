#
# [342] Power of Four
#
# https://leetcode.com/problems/power-of-four/description/
#
# algorithms
# Easy (39.03%)
# Total Accepted:    81.2K
# Total Submissions: 208.1K
# Testcase Example:  '16'
#
# 
# Given an integer (signed 32 bits), write a function to check whether it is a
# power of 4.
# 
# Example:
# Given num = 16, return true.
# Given num = 5, return false.
# 
# 
# Follow up: Could you solve it without loops/recursion?
# 
# Credits:Special thanks to @yukuairoy  for adding this problem and creating
# all test cases.
#
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 1 star
        if num == 1:
            return True
        if num == 0 or num % 4 != 0:
            return False
        return self.isPowerOfFour(num//4)
        
