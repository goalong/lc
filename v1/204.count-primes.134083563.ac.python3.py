#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (26.58%)
# Total Accepted:    146.9K
# Total Submissions: 553K
# Testcase Example:  '0'
#
# Description:
# Count the number of prime numbers less than a non-negative number, n.
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
#
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 6 star. must master.
        # 其思想是从小的素数开始，排除该小素数的所有倍数，直到最终剩下的全是素数
        if n < 3:
            return 0
        data = [1] * n
        data[0], data[1] = 0, 0
        for i in range(2, int(n**0.5)+1):
            if data[i]:
                for j in range(2*i, n, i):
                    data[j] = 0
        return sum(data)
