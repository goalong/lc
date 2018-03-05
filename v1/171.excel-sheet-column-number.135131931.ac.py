#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (48.30%)
# Total Accepted:    159.9K
# Total Submissions: 331.1K
# Testcase Example:  '"A"'
#
# Related to question Excel Sheet Column Title
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
# 
# For example:
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28 
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 3 star.
        rs = 0
        for c in s:
            rs = rs*26 + ord(c) - ord("A") + 1
        return rs

