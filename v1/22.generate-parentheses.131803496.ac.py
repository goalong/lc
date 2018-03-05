#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (47.56%)
# Total Accepted:    196.6K
# Total Submissions: 413.4K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rs = []
        self.helper(n, n, '', rs)
        return rs

    def helper(self, left, right, current, rs):
    	if left == right == 0:
    		rs.append(current)
    		return
    	if left > 0:
    		self.helper(left-1, right, current+'(', rs)
    	if right > left:
    		self.helper(left, right-1, current + ')', rs)
        

