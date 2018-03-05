#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (24.63%)
# Total Accepted:    444.9K
# Total Submissions: 1.8M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# Examples:
# 
# Given "abcabcbb", the answer is "abc", which the length is 3.
# 
# Given "bbbbb", the answer is "b", with the length of 1.
# 
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the
# answer must be a substring, "pwke" is a subsequence and not a substring.
#
class Solution(object):
    def lengthOfLongestSubstring(self, s):  # 
        """
        :type s: str
        :rtype: int
        """
        max_len, start = 0, 0
        memo = {}
        for i, char in enumerate(s):
            if char not in memo or memo[char] < start:
                max_len = max(max_len, i + 1 - start)
            else:
                start = memo[char] + 1    
            memo[char] = i
        return max_len

