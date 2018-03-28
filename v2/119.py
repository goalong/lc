



class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # 6 star, 没理解
        # todo, 回头看
        result = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                result[i - j] += result[i - j - 1]
        return result


# print(Solution().getRow(2))
