



class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # 6 star, 没理解
        result = [0] * (rowIndex + 1)
        result[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                result[j] += result[j-1]
        return result


print(Solution().getRow(3))
