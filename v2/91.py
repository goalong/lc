




class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp, 6 star, 还没理解，需重看, 几个情况的分类讨论需要注意
        # 分类讨论, dp[i]表示前i个字符的最多解码方式
        if s == "" or s[0] == "0":
            return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[:2] = [1, 1]
        for i in range(2, n+1):
            before = int(s[i-2:i])
            if 26 >= before > 10 and before != 20: # 大于10小于26且不等于20的，有两种情况，一种是dp[i-1] 一种是dp[i-2]
                dp[i] = dp[i-1] + dp[i-2]
            elif before in (10, 20): # 10 和 20 只能有一种解码方式，所以等于 dp[i-2]
                dp[i] = dp[i-2]
            elif 9 >= int(s[i-1]) >= 1: #  这种是大于26且各位上不是0的 等于 dp[i-1]
                dp[i] = dp[i-1]
            # 剩余的就是大于26且个位是0的了，例如 40 50，这种根本无法解码，所以dp[i]=0
        return dp[-1]

# print(Solution().numDecodings("100"))
