#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (45.82%)
# Total Accepted:    59.8K
# Total Submissions: 130.5K
# Testcase Example:  '"abccccdd"'
#
# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
# 
# This is case sensitive, for example "Aa" is not considered a palindrome
# here.
# 
# Note:
# Assume the length of given string will not exceed 1,010.
# 
# 
# Example: 
# 
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# 
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        rs = 0
        memo = {}
        for char in s:
            memo[char] = memo.get(char, 0) + 1
        odd = 0
        for k,v in memo.items():
            if v % 2 == 0:
                rs += v
            else:
                odd = 1
                rs += v - 1
        return rs + odd
