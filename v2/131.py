




class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # 6 star, 必须掌握
        # 辅助函数判断字符串是否回文很重要
        #
        rs = []
        self.dfs([], rs, s)
        return rs

    def is_palindrome(self, s):
        n = len(s)
        for i in range(n//2 + 1):
            if s[i] != s[n-1-i]:
                return False
        return True

    def dfs(self, path, rs, s):
        if s == "":
            rs.append(path)
            return
        for i in range(1, len(s)+1):
            if self.is_palindrome(s[:i]):
                self.dfs(path+[s[:i]], rs, s[i:])


print(Solution().partition("aab"))