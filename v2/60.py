



class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # 6 star. 必须掌握
        # 解法非常巧妙，共有n!个序列，除了首位有(n-1)!个序列，k//(n-1)!可以确定首位，后续的每一位可以依次按照此规则计算出

        k -= 1
        fact = 1
        for i in range(1, n):
            fact *= i
        rs = ""
        nums = list(range(1, 10))
        for i in range(n-1, -1, -1):
            index = k // fact
            num = nums.pop(index)
            rs += str(num)
            if i > 0:
                k %= fact
                fact //= i
        return rs

# print(Solution().getPermutation(5, 80))