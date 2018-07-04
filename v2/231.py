


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 2 star, 不断除以2
        if n < 1:
            return False
        while n >= 2:
            if n % 2 == 1:
                return False
            n = n // 2
        return True