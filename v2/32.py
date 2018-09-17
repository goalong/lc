



class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 动态规划 参考 https://shenjie1993.gitbooks.io/leetcode-python/032%20Longest%20Valid%20Parentheses.html
        # 6 star, 还需多看
        # dp[i]表示以i为末尾的最大长度，只有当i位置上是右括号时dp[i]才可能大于0，j表示当前有效子字符串的前一位，如果j上是左括号
        # 则dp[i] = dp[i - 1] + 2，即加了i和j这两个，并且还要检验j-1上的最大长度，因为有可能两个子字符串连接起来
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