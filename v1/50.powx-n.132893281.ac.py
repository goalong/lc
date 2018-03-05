#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (26.03%)
# Total Accepted:    200K
# Total Submissions: 768.5K
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n).
# 
# 
# 
# 
# Example 1:
# 
# Input: 2.00000, 10
# Output: 1024.00000
# 
# 
# 
# Example 2:
# 
# Input: 2.10000, 3
# Output: 9.26100
# 
# 
#
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 4 star.
        if n == 0:
            return 1.0
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2:
            return self.myPow(x*x,n/2)*x
        else:
            return self.myPow(x*x,n/2)
