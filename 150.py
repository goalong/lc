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
