




class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # 6 star, 求路径和最小值， 最大最小值首先考虑动态规划， 从底层到顶层按层遍历，
        # 状态转移方程 dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        length = len(triangle)
        dp = triangle[-1]
        for i in range(length-2, -1, -1):
            for j in range(i+1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]
