


class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 4 star, 解法很巧妙
        for i in (2, 3, 5):
            while num % i == 0:
                num = num // i
        return num == 1
