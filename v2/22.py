



class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 6 star, dfs, left right分别是剩余的左右括号的数量，
        rs = []
        self.helper(n, n, "", rs)
        return rs

    def helper(self, left, right,  path, rs):
        if left == 0 and right == 0:
            rs.append(path)
            return
        if left > 0:
            self.helper(left-1, right, path+"(", rs)
        if right > left:    # 注意这个条件，只有剩余的右括号比左括号多时，才会加右括号
            self.helper(left, right-1, path+")", rs)
