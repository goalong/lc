#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (33.27%)
# Total Accepted:    71.7K
# Total Submissions: 215.5K
# Testcase Example:  '1'
#
# 
# Write a program to find the n-th ugly number.
# 
# 
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
# 
# 
# 
# Note that 1 is typically treated as an ugly number, and n does not exceed
# 1690.
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        num = 1
        index = 1
        while index < n:
            num += 1
            if self.is_ugly(num):
                index += 1

        return num

    def is_ugly(self, num):
        if num <= 0:
            return False
        for i in (2, 3, 5):
            while num % i == 0:
                num = num // i
        return num == 1
