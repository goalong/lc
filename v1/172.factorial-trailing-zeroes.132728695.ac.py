#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (36.85%)
# Total Accepted:    112K
# Total Submissions: 303.9K
# Testcase Example:  '0'
#
# Given an integer n, return the number of trailing zeroes in n!.
# 
# Note: Your solution should be in logarithmic time complexity.
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 6 star, 很精巧，必须掌握
        # 所有的尾部的0可以看做都是2*5得来的，所以通过计算所有的因子中2和5的个数就可以知道尾部0的个数。
        # 实际上，2的个数肯定是足够的，所以只需计算5的个数即可。 
        # 要注意，25=5*5是有两个5的因子；125=5*5*5有3个5的因子。比如，计算135!末尾0的个数。 
        # 首先135/5 = 27，说明135以内有27个5的倍数；27/5=5，说明135以内有5个25的倍数；
        # 5/5=1，说明135以内有1个125的倍数。当然其中有重复计数，算下来135以内因子5的个数为27+5+1=33。
        rs = 0
        while n > 0:
            n /= 5
            rs += n
        return rs
            
        
