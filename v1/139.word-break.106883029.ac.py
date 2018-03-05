#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (31.31%)
# Total Accepted:    199.4K
# Total Submissions: 636.9K
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# 
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words. You may assume the dictionary does
# not contain duplicate words.
# 
# 
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
# 
# 
# 
# Return true because "leetcode" can be segmented as "leet code".
# 
# 
# 
# UPDATE (2017/1/4):
# The wordDict parameter had been changed to a list of strings (instead of a
# set of strings). Please reload the code definition to get the latest changes.
# 
#
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        d = set(wordDict)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in d:
                    dp[i] = True
        return dp[n]
