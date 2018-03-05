#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (38.00%)
# Total Accepted:    140K
# Total Submissions: 368.4K
# Testcase Example:  '0'
#
# Given an index k, return the kth row of the Pascal's triangle.
# 
# 
# For example, given k = 3,
# Return [1,3,3,1].
# 
# 
# 
# Note:
# Could you optimize your algorithm to use only O(k) extra space?
# 
#
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # 2 star. my solution is stupid
        if rowIndex < 0:
            return []
        if rowIndex == 0:
            return [1]
        last_row = [1]
        i = 2
        while i < rowIndex + 2:
            index = 1
            new_row = [1] * i
            while index < i:
                _last = last_row[index] if index < len(last_row) else 0
                new_row[index] = last_row[index - 1] + _last
                index += 1
            last_row = new_row
            i += 1
        return new_row
