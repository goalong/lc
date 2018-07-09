
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 5 star, 从左上角位置的元素开始进行比较，如果比目标值大，则排除所在的列，将列的值减一，
        # 如果比目标值小，则排除所在的行，将行值加一
        # 左上角的值是所在行的最大值，所在列的最小值，与其对比进行排除
        if not matrix or not matrix[0]:
            return False
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
