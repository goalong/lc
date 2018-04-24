


class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 4 star, 相当于一个26进制的转换，从最末开始，逐个向前，每个位上的值乘以对应的数
        count = 0
        rs = 0
        while s:
            rs += (ord(s[-1]) - ord("A") + 1) * (26 ** count)
            count += 1
            s = s[:-1]
        return rs

# print(Solution().titleToNumber("AA"))
