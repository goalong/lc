




class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 6 star, 需要熟练，先将矩阵沿着对角线翻转，再上下翻转，就可以实现顺时针旋转90度的效果
        # 参考： https://shenjie1993.gitbooks.io/leetcode-python/048%20Rotate%20Image.html
        n = len(matrix)
        for row in range(n):
            for column in range(n - row):
                matrix[row][column], matrix[n - 1 - column][n - 1 - row] = matrix[n - 1 - column][n - 1 - row], \
                                                                           matrix[row][column]
        matrix.reverse()