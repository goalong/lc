



class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 6 star, 遍历时寻找最小值以及比较最大的差值
        if len(prices) <= 1:
            return 0
        rs = 0
        low = prices[0]
        for i in prices:
            rs = max(rs, i - low)
            if i < low:
                low = i
        return rs