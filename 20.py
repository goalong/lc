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
