#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (28.75%)
# Total Accepted:    214.1K
# Total Submissions: 744.7K
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x.
# 
# x is guaranteed to be a non-negative integer.
# 
# 
# 
# Example 1:
# 
# Input: 4
# Output: 2
# 
# 
# 
# Example 2:
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we want to return
# an integer, the decimal part will be truncated.
# 
# 
#
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 5 star.
        if x == 0 or x == 1:
            return x
        low = 0
        high = x
        while low < high:
            middle = (low + high) // 2
            cur = middle * middle
            if cur < x:
                low = middle + 1
            elif cur > x:
                high = middle
            else:
                return middle
        if middle * middle < x and (middle+1)**2 > x:
            return middle
        return middle - 1

