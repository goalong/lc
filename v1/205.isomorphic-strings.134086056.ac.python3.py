#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (34.60%)
# Total Accepted:    130.2K
# Total Submissions: 376.2K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
# 
# For example,
# Given "egg", "add", return true.
# 
# Given "foo", "bar", return false.
# 
# Given "paper", "title", return true.
# 
# Note:
# You may assume both s and t have the same length.
#
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 2 star.
        s2t = {}
        t2s = {}
        for index, char in enumerate(s):
            if char not in s2t:
                s2t[char] = t[index]
                if t[index] not in t2s:
                    t2s[t[index]] = char
                elif t[index] in t2s and t2s[t[index]] != char:
                    return False
            else:
                if s2t[char] != t[index]:
                    return False
        return True

        
