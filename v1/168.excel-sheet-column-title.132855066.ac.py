#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (27.16%)
# Total Accepted:    129.9K
# Total Submissions: 478.2K
# Testcase Example:  '1'
#
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
# 
# For example:
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# 
# Credits:Special thanks to @ifanchu for adding this problem and creating all
# test cases.
#
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 3 star.
        rs = []
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while n > 0:
            index = (n - 1) % 26   #
            rs.append(letters[index])
            n = (n - 1) // 26 if index != 0 else n // 26
        return "".join(rs[::-1])
