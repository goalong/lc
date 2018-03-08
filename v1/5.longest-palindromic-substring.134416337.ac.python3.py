#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (25.18%)
# Total Accepted:    290.1K
# Total Submissions: 1.2M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example:
# 
# 
# Input: "babad"
# 
# Output: "bab"
# 
# Note: "aba" is also a valid answer.
# 
# 
# 
# 
# Example:
# 
# 
# Input: "cbbd"
# 
# Output: "bb"
# 
# 
# 
# 
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 6 star, this solution is too slow. 思路十分巧妙
        res = ""
        for i in range(len(s)):
            res = max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)

        return res
       
    # 关键的是这个辅助方法
    def helper(self,s,l,r):
        
        while 0<=l and r < len(s) and s[l]==s[r]:
                l-=1; r+=1
        return s[l+1:r]
