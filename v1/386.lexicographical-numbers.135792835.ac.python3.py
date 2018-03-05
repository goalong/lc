#
# [386] Lexicographical Numbers
#
# https://leetcode.com/problems/lexicographical-numbers/description/
#
# algorithms
# Medium (42.18%)
# Total Accepted:    27.2K
# Total Submissions: 64.4K
# Testcase Example:  '13'
#
# 
# Given an integer n, return 1 - n in lexicographical order.
# 
# 
# 
# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
# 
# 
# 
# Please optimize your algorithm to use less time and space. The input size may
# be as large as 5,000,000.
# 
#
from functools import cmp_to_key
class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # 3 star.
        def _cmp(a, b):
            if str(a) > str(b):
                return 1
            elif str(a) < str(b):
                return -1
            return 0
        l = list(range(1, n+1))

        return sorted(l, key=cmp_to_key(_cmp))

