#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (30.26%)
# Total Accepted:    103.8K
# Total Submissions: 343K
# Testcase Example:  '[]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# Design an algorithm to find the maximum profit. You may complete at most two
# transactions.
# 
# Note:
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        rs = []
        _min = prices[0]
        i = 0
        while i < len(prices):
            if i == len(prices) - 1:
                if prices[i] > _min:
                    rs.append(prices[i] - _min)
            else:
                if prices[i] > prices[i+1]:
                    rs.append(prices[i] - _min)
                    _min = prices[i+1]
            i += 1
        rs.sort()
        return sum(rs[-2:])
