





class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 5 star 动态规划 dp[x] = dp[x-1] + dp[x-2]
        a, b = 1, 2
        for _ in range(n-1):
            a, b = b, a+b
        return a