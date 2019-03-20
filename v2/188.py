class Solution(object):

    # 7 star, no idea, 下面的解法来自： https://www.hrwhisper.me/leetcode-best-time-to-buy-and-sell-stock-i-ii-iii-iv/
    def maxProfit(self, k, prices):
        n = len(prices)
        if k >= (n >> 1): return self.maxProfit2(prices)
        dp = [[0 for j in range(n)] for i in range(k + 1)]

        for i in range(1, k + 1):
            maxTemp = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + maxTemp)
                maxTemp = max(maxTemp, dp[i - 1][j - 1] - prices[j])
        return dp[k][n - 1]

    def maxProfit2(self, prices):
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                ans += prices[i] - prices[i - 1]
        return ans