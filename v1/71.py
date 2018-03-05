class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        stack = []
        for i in path:
            if i in ('.', ''):
                continue
            elif i == '..':
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(i)
        rs = '/' + "/".join(stack)
        return rs


# s = Solution()
# print(s.simplifyPath('/../home/'))
# print(s.simplifyPath('/home/..'))
# print(s.simplifyPath("/a//b/../../c/d/../../..//"))

