



class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 5 star, 利用栈先进后出的特性，遇到符号的左半部分就入栈，遇到右半部分就检查栈顶的元素是不是对应的左括号，是的话就出栈
        # 最后如果栈是空的话则是合规的
        stack = []
        data = {"(": ")", "[": "]", "{": "}"}
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if stack and data.get(stack[-1]) == i:
                    stack.pop()
                else:
                    stack.append(i)
        return len(stack) == 0