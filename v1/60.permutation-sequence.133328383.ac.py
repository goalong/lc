#
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (29.35%)
# Total Accepted:    98.8K
# Total Submissions: 336.6K
# Testcase Example:  '1\n1'
#
# The set [1,2,3,…,n] contains a total of n! unique permutations.
# 
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# 
# Given n and k, return the kth permutation sequence.
# 
# Note: Given n will be between 1 and 9 inclusive.
#
class Solution(object):
    def getPermutation(self, n, k):
        # 6 star. must master.
        
        res = ''
        k -= 1
        fac = 1
        for i in range(1, n):
            fac *= i
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in reversed(range(n)):
            curr = num[k // fac]
            res += str(curr)
            num.remove(curr)
            if i != 0:
                k %= fac
                fac //= i
        return res
