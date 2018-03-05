#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (33.40%)
# Total Accepted:    99K
# Total Submissions: 296.5K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# ⁠Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
# 
# Examples:
# 
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# 
# 
# 
# 
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters separated by a single space.
# 
# 
# Credits:Special thanks to @minglotus6 for adding this problem and creating
# all test cases.
#
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # 4 star.
        str_list = str.split(" ")
        memo = {}
        _memo = {}
        if len(pattern) != len(str_list):
            return False
        for index, char in enumerate(pattern):
            if char in memo:
                if memo[char] != str_list[index]:
                    return False
            else:
                memo[char] = str_list[index]
                if str_list[index] in _memo and _memo[str_list[index]] != char:
                    return False
                else:
                    _memo[str_list[index]] = char


        return True

