



class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 动态规划 参考 https://shenjie1993.gitbooks.io/leetcode-python/032%20Longest%20Valid%20Parentheses.html
        # 6 star, 还需多看
        if not s:
            return 0
        length = len(s)
        dp = [0 for _ in range(length)]
        for i in range(1, length):
            if s[i] == ")":
                j = i - 1 - dp[i - 1]
                if j >= 0 and s[j] == "(":
                    dp[i] = dp[i - 1] + 2
                    if j - 1 >= 0:
                        dp[i] += dp[j - 1]
        return max(dp)