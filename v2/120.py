




class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # 6 star, 求路径和最小值， 最大最小值首先考虑动态规划， 从底层到顶层按层遍历，
        # 状态转移方程 dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        # dp[i]表示从底层到当前层的第i个元素的路径中最小的和，比较巧妙
        length = len(triangle)
        dp = triangle[-1]
        for i in range(length-2, -1, -1): # 从倒数第二行开始，一直到第一行
            for j in range(i+1):   # 在每一行计算时，从前到后
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]
