


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 6 star, no idea
        # dp[i][j]表示以坐标（i,j)为右下角的全是1的正方形的最大边长，
        # 状态转移方程 dp[j][i] = min(dp[j-1][i], dp[j][i-1], dp[j-1][i-1]) + 1
        if not matrix:
            return 0
        row_num = len(matrix)
        col_num = len(matrix[0])
        dp = [[0 for _ in range(col_num)] for _ in range(row_num)]
        max_width = 0
        for i in range(col_num):
            for j in range(row_num):
                dp[j][i] = int(matrix[j][i])
                if dp[j][i] and j > 0 and i > 0:
                    dp[j][i] = min(dp[j-1][i], dp[j][i-1], dp[j-1][i-1]) + 1
                max_width = max(max_width, dp[j][i])
        return max_width * max_width

