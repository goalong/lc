#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (33.94%)
# Total Accepted:    305.6K
# Total Submissions: 900.4K
# Testcase Example:  '"["'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# The brackets must close in the correct order, "()" and "()[]{}" are all valid
# but "(]" and "([)]" are not.
# 
#
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = "([{"
        stack = []
        for i in s:
            if i in left:
                stack.append(i)
            else:
                if not stack:
                    return False
                if i == ")" and stack[-1] != '(':
                    return False
                elif i == "}" and stack[-1] != "{":
                    return False
                elif i == "]" and stack[-1] != '[':
                    return False
                else:
                    stack.pop()
        return not stack

