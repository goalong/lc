


# 题意:给定股票每日的售价，求最多两次买卖最多可以获取多大利润？

# class Solution:
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         # 5 star, 其实就是找到几个连续的单调递增子数组，子数组的首尾差值存到一个列表中，对列表排序，将列表中最大的两个求和，
#         # 这个方法错了，比如对于[1,2,4,2,5,7,2,4,9,0]， 结果该是13， 而该方法得到12
#         length = len(prices)
#         if length <= 1:
#             return 0
#         rs = []
#         low = prices[0]
#         index = 0
#         while index < length:
#             if index == length - 1:
#                 if prices[index] > low:
#                     rs.append(prices[index] - low)
#             else:
#                 if prices[index] > prices[index+1]:
#                     rs.append(prices[index] - low)
#                     low = prices[index+1]
#             index += 1
#         rs.sort()
#         return sum(rs[-2:])




class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        # 6 star, todo, 没有理解，几次做错了
        # https://www.hrwhisper.me/leetcode-best-time-to-buy-and-sell-stock-i-ii-iii-iv/
        #  动态规划，dp[i]表示到第i天能获取的最大收益，两次操作的最大收益等于第i天之后的最大价格减去第i天的价格加上dp[i-1]
        # dp[i] = max(dp[i-1], prices[i]-min_price)
        if not prices: return 0
        dp = [0] * len(prices)
        min_price = prices[0]
        for i in range(1, len(prices)):
            dp[i] = max(dp[i - 1], prices[i] - min_price)
            min_price = min(prices[i], min_price)

        ans = dp[-1]
        max_price = prices[-1]
        for i in range(len(prices) - 2, 0, -1):
            ans = max(ans, max_price - prices[i] + dp[i - 1])
            max_price = max(max_price, prices[i])

        return ans


print(Solution().maxProfit([1,2,4,2,5,7,2,4,9,0]))