



class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 3 star.
        rs = ""
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while n > 0:
            extra = (n-1) % 26
            rs = letters[extra] + rs
            n = (n - extra) // 26
        return rs

# print(Solution().convertToTitle(1265))
