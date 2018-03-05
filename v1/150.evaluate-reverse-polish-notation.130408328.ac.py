#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (28.26%)
# Total Accepted:    111.1K
# Total Submissions: 393.3K
# Testcase Example:  '["18"]'
#
# 
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# 
# 
# 
# Valid operators are +, -, *, /. Each operand may be an integer or another
# expression.
# 
# 
# 
# Some examples:
# 
# ⁠ ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
# ⁠ ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
# 
# 
#
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        import operator
        stack = []
        op_map = {"+": operator.add, '-': operator.sub,
                  "*": operator.mul, '/': operator.div}
        for i in tokens:
            if i in "+-*/":
                last = stack.pop()
                second_last = stack.pop()
                rs = op_map[i](second_last, last)
                if i == '/' and rs < 0 and second_last % last:   # remark: integer division floors
                	rs += 1
                stack.append(rs)
            else:
                stack.append(int(i))
        return stack[-1]

# s = Solution()
# print(s.evalRPN(["4","-2","/","2","-3","-","-"]))
# print(s.evalRPN(["10", "6", "9", "3", '+', '-11', '*', '/', '*', "17", '+', '5', '+']))

