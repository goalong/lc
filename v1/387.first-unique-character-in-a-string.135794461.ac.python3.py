#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (47.23%)
# Total Accepted:    107.3K
# Total Submissions: 227.3K
# Testcase Example:  '"leetcode"'
#
# 
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.
# 
# 
# 
# 
# Note: You may assume the string contain only lowercase letters.
# 
#
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1 star
        memo = {}
        for index, char in enumerate(s):
            memo[char] = memo.get(char, 0) + 1
        for i in range(len(s)):
            if memo[s[i]] == 1:
                return i
        return -1
