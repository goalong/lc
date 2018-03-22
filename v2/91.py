




class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp, 6 star, 还没理解，需重看, 几个情况的分类讨论需要注意
        if s == "" or s[0] == "0":
            return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[:2] = [1, 1]
        for i in range(2, n+1):
            before = int(s[i-2:i])
            if 26 >= before > 10 and before != 20:
                dp[i] = dp[i-1] + dp[i-2]
            elif before in (10, 20):
                dp[i] = dp[i-2]
            elif 9 >= int(s[i-1]) >= 1:
                dp[i] = dp[i-1]
        return dp[-1]

# print(Solution().numDecodings("100"))
