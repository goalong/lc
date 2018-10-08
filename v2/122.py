



class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 6 star, 从左到右遍历，如果当前比后面的一个数值大，则将当前和之前记录的较小值的差加到结果中，并设后面的为较小值， 注意最后一个的边界条件
        length = len(prices)
        if length <= 1:
            return 0
        low = prices[0]
        index = 0
        rs = 0
        while index < length:
            if index == length - 1:
                if prices[index] > low:
                    rs += prices[index] - low
            else:
                if prices[index] > prices[index+1]:
                    rs += prices[index] - low
                    low = prices[index+1]
            index += 1
        return rs

print(Solution().maxProfit([2, 1, 4]))