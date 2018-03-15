




class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 6 star,
        # 动态规划，状态转移方程： dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, n):
            for j in range(1, m):
                dp[j][i] = dp[j][i-1] + dp[j-1][i]
        return dp[-1][-1]