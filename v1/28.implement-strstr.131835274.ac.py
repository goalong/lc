#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (28.87%)
# Total Accepted:    252.6K
# Total Submissions: 875K
# Testcase Example:  '"hello"\n"ll"'
#
# 
# Implement strStr().
# 
# 
# 
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
# 
# 
# Example 1:
# 
# Input: haystack = "hello", needle = "ll"
# Output: 2
# 
# 
# 
# Example 2:
# 
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# 
# 
#
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 中文测试
        index = -1
        needle_len = len(needle)
        for i in range(len(haystack) - needle_len + 1):
        	if haystack[i:i+needle_len] == needle:
        		index = i
        		break
        return index
        


print(Solution().strStr('abder', 'r'))
