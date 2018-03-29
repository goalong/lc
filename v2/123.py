



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
        # 6 star, todo, 没有理解
        # https://www.hrwhisper.me/leetcode-best-time-to-buy-and-sell-stock-i-ii-iii-iv/
        if not prices:
            return 0
        n = len(prices)
        dp, money, profit = [], prices[0], 0
        for i in range(n):
            profit = max(profit, prices[i] - money)
            money = min(money, prices[i])
            dp.append(profit)

        i, ans, money, profit = n - 1, dp[n - 1], prices[n - 1], 0
        while i >= 0:
            profit = max(profit, money - prices[i])
            money = max(money, prices[i])
            ans = max(ans, dp[i] + profit)
            i -= 1
        return ans


print(Solution().maxProfit([1,2,4,2,5,7,2,4,9,0]))