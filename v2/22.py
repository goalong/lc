
#
#
#
# class Solution:
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#
#         # 5 star, 优先添加左括号，当剩余的右括号比左括号多时可以添加右括号
#         # dfs, left right分别是剩余的左右括号的数量，
#         rs = []
#         self.helper(n, n, "", rs)
#         return rs
#
#     def helper(self, left, right,  path, rs):
#         if left == 0 and right == 0:
#             rs.append(path)
#             return
#         if left > 0:
#             self.helper(left-1, right, path+"(", rs)
#         if right > left:    # 注意这个条件，只有剩余的右括号比左括号多时，才会加右括号
#             self.helper(left, right-1, path+")", rs)


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rs = []
        path = ""
        self.dfs(n, n, path, rs)
        return rs

    def dfs(self, left, right, path, rs):
        if left == 0 and right == 0:
            rs.append(path)
            return
        if left > 0:
            self.dfs(left - 1, right, path + "(", rs)

        if right > left:
            self.dfs(left, right - 1, path + ")", rs)


print(Solution().generateParenthesis(3))