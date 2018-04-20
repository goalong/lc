


class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        rs = 0
        while s:
            rs += (ord(s[-1]) - ord("A") + 1) * (26 ** count)
            count += 1
            s = s[:-1]
        return rs

# print(Solution().titleToNumber("AA"))
