class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 3 star, no idea, 位操作没掌握好
        r = 0
        while n:
            r += n & 1
            n >>= 1
        return r
        