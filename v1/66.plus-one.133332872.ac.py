#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (39.58%)
# Total Accepted:    224.7K
# Total Submissions: 567.6K
# Testcase Example:  '[0]'
#
# Given a non-negative integer represented as a non-empty array of digits, plus
# one to the integer.
# 
# You may assume the integer do not contain any leading zero, except the number
# 0 itself.
# 
# The digits are stored such that the most significant digit is at the head of
# the list.
#
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 1 star.
        extra = 0
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + extra > 9:
                digits[i] = 0
                extra = 1
            else:
                digits[i] += extra
                extra = 0
        if extra == 1:
            digits.insert(0, 1)
        return digits
