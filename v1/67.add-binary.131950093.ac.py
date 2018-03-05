#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (33.86%)
# Total Accepted:    189.7K
# Total Submissions: 560.2K
# Testcase Example:  '"0"\n"0"'
#
# 
# Given two binary strings, return their sum (also a binary string).
# 
# 
# 
# For example,
# a = "11"
# b = "1"
# Return "100".
# 
#
class Solution(object):
    def addBinary(self, a, b):  # 1 star,
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a and not b:
            return ''
        a_list = list(a)
        b_list = list(b)
        extra = 0
        rs = []
        total = 0
        while a_list or b_list:
            cur_a = int(a_list.pop()) if a_list else 0
            cur_b = int(b_list.pop()) if b_list else 0
            total = cur_b + cur_a + extra

            extra = 1 if total > 1 else 0
            total = total - 2 if total > 1 else total
            rs.append(str(total))
        if extra:
            rs.append(str(extra))
        return ''.join(rs[::-1])


# s = Solution()
# print(s.addBinary('101', '101'))

