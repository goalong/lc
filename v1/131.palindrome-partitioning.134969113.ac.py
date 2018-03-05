#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (35.34%)
# Total Accepted:    116K
# Total Submissions: 328.3K
# Testcase Example:  '"aab"'
#
# 
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# 
# Return all possible palindrome partitioning of s.
# 
# 
# For example, given s = "aab",
# 
# Return
# 
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
# 
#
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # 6 star, must master.
        rs = []
        self.dfs([], s, rs)
        return rs

    def is_palindrome(self, s):
        for i in range(len(s)):
            if s[i] != s[len(s)-1-i]:
                return False
        return True

    def dfs(self, path,s,  rs):
        if len(s) == 0:
            rs.append(path)
            return
        for i in range(1, len(s)+1):
            if self.is_palindrome(s[:i]):
                self.dfs(path+[s[:i]], s[i:], rs)
