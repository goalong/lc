




class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # 6 star, 动态规划， 注意要特殊处理最上和左的行和列
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[j][i]:
                    dp[j][i] = 0
                else:
                    dp[j][i] = dp[j-1][i] + dp[j][i-1]
        return dp[-1][-1]

# a = [[0,0,0],
#      [1,0,0],
#      [0,0,0]]
# # a = [[1]]
# print(Solution().uniquePathsWithObstacles(a))
