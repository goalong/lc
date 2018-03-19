




class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 5 star, 先用两个列表记录哪个行或列的值为0， 然后遍历matrix，如果某位置的行或列为0，则该位置为0
        cols = [0 for _ in range(len(matrix))]
        rows = [0 for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    cols[i], rows[j] = 1, 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if cols[i] or rows[j]:
                    matrix[i][j] = 0
