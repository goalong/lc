



class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 栈
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