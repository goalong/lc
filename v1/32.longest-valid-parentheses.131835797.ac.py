#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (23.22%)
# Total Accepted:    119.2K
# Total Submissions: 513.4K
# Testcase Example:  '""'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# 
# 
# For "(()", the longest valid parentheses substring is "()", which has length
# = 2.
# 
# 
# Another example is ")()())", where the longest valid parentheses substring is
# "()()", which has length = 4.
# 
#
class Solution(object):
    def longestValidParentheses(self, s):

        """
        copy的思路:
        这道求最长有效括号比之前那道 Valid Parentheses 验证括号难度要大一些，
        这里我们还是借助栈来求解，需要定义个start变量来记录合法括号串的起始位置，
        我们遍历字符串，如果遇到左括号，则将当前下标压入栈，如果遇到右括号，如果当前栈为空，
        则将下一个坐标位置记录到start，如果栈不为空，则将栈顶元素取出，此时若栈为空，
        则更新结果和i - start + 1中的较大值，否则更新结果和i - 栈顶元素中的较大值
        """
        maxlen = 0
        stack = []
        start = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  # push the INDEX into the stack!!!!
            else:
                if stack == []:
                    start = i + 1
                else:  # 有未匹配的左括号
                    stack.pop()
                    if stack == []:
                        maxlen = max(maxlen, i - start + 1)
                    else:
                        maxlen = max(maxlen, i - stack[-1])
        return maxlen


# s = Solution()
# print(s.longestValidParentheses('(()))())('))
# print(s.longestValidParentheses('()'))
# print(s.longestValidParentheses('))()(()'))
