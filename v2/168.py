class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 4 star, 进制转换，26进制
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ret = ""
        while n > 0:
            n, extra = divmod(n - 1, 26)  # 注意这里需要用n-1而不是n对26进行divmod运算
            ret += letters[extra]
        return ret[::-1]




