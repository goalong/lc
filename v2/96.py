





class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 6 star, 动态规划， 需多练
        # dp[i]表示i 个数字能组成的树的个数
        # 状态转移方程： dp[0], dp[1], dp[2] = 1, 1, 2, 对于n>2, dp[n] = dp[0]*dp[n-1] +dp[1]*dp[[n-2] + ..+dp[n-1]*dp[0]
        if n < 3:
            dp = [1, 1, 2]
            return dp[n]
        else:
            dp = [0 for _ in range(n+1)]
            dp[:3] = [1, 1, 2]
            for i in range(3, n+1):
                for j in range(i):
                    dp[i] += dp[j] * dp[i-j-1]
            return dp[-1]