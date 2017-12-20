class Solution(object):
    def spiralOrder(self, matrix):  # 3 star, no idea
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rs = []
        while matrix:
            if matrix[0]:
                rs.extend(matrix.pop(0))
            if matrix and matrix[0]:
                for row in matrix:
                    rs.append(row.pop())
            if matrix:
                rs += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    rs.append(row.pop(0))
        return rs
        