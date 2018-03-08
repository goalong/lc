#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (31.63%)
# Total Accepted:    251.3K
# Total Submissions: 794.5K
# Testcase Example:  '[]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# 这个思路很明显，从头开始对比列表中每个字符串
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        index = 0
        while True:
            for s in strs:
                if len(s) <= index or s[index] != strs[0][index]:
                    return strs[0][:index]
            index += 1


# s = Solution()
# print s.longestCommonPrefix(['abc', 'abccd'])
