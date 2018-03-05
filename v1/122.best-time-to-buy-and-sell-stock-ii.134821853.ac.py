#
# [122] Best Time to Buy and Sell Stock II
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
#
# algorithms
# Easy (47.78%)
# Total Accepted:    190.7K
# Total Submissions: 399.2K
# Testcase Example:  '[]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (ie, buy one and sell one share of the stock
# multiple times). However, you may not engage in multiple transactions at the
# same time (ie, you must sell the stock before you buy again).
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        rs = 0
        _min = prices[0]
        i = 0
        while i < len(prices):
            if i == len(prices) - 1:
                if prices[i] > _min:
                    rs += prices[i] - _min
            else:
                if prices[i] > prices[i+1]:
                    rs += prices[i] - _min
                    _min = prices[i+1]
            i += 1
        return rs
