#
# [316] Remove Duplicate Letters
#
# https://leetcode.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Hard (30.32%)
# Total Accepted:    38.3K
# Total Submissions: 126.4K
# Testcase Example:  '"bcabc"'
#
# 
# Given a string which contains only lowercase letters, remove duplicate
# letters so that every letter appear once and only once. You must make sure
# your result is the smallest in lexicographical order among all possible
# results.
# 
# 
# 
# Example:
# 
# 
# Given "bcabc"
# Return "abc"
# 
# 
# Given "cbacdcbc"
# Return "acdb"
# 
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(set(s))
        s.sort()
        return "".join(s)
