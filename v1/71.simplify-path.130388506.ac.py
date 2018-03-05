#
# [71] Simplify Path
#
# https://leetcode.com/problems/simplify-path/description/
#
# algorithms
# Medium (26.20%)
# Total Accepted:    108.6K
# Total Submissions: 414.4K
# Testcase Example:  '"/"'
#
# Given an absolute path for a file (Unix-style), simplify it.
# 
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# 
# 
# click to show corner cases.
# 
# Corner Cases:
# 
# 
# 
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together,
# such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".
# 
# 
#
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


