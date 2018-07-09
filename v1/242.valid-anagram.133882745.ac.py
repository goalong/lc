#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (47.31%)
# Total Accepted:    201.2K
# Total Submissions: 425.3K
# Testcase Example:  '""\n""'
#
# Given two strings s and t, write a function to determine if t is an anagram
# of s. 
# 
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
# 
# 
# Note:
# You may assume the string contains only lowercase alphabets.
# 
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
#
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 3 star, 将两个字符串分别排序，比较排序后的结果是否相同
        _s = sorted(s)
        _t = sorted(t)
        return _s == _t
        
