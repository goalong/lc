#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (46.74%)
# Total Accepted:    221.1K
# Total Submissions: 473.2K
# Testcase Example:  '[1,2,3]'
#
# 
# Given a collection of distinct numbers, return all possible permutations.
# 
# 
# 
# For example,
# [1,2,3] have the following permutations:
# 
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#
class Solution(object):
    def permute(self, num):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(num) == 0:
            return []
        if len(num) == 1:
            return [num]
        rs = []
        for i in range(len(num)):
            for j in self.permute(num[:i]+num[i+1:]):
                rs.append([num[i]] + j)
        return rs
