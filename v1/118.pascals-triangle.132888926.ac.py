#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (39.85%)
# Total Accepted:    163.2K
# Total Submissions: 409.5K
# Testcase Example:  '0'
#
# Given numRows, generate the first numRows of Pascal's triangle.
# 
# 
# For example, given numRows = 5,
# Return
# 
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
# 
#
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 2 star. my solution is stupid
        if numRows < 1:
            return []
        rs = [[1]]
        i = 2
        while i < numRows + 1:
            index = 1
            last_row = rs[-1]
            new_row = [1] * i
            while index < i:
                _last = last_row[index] if index < len(last_row) else 0
                new_row[index] = last_row[index - 1] + _last
                index += 1
            rs.append(new_row)
            i += 1
        return rs
