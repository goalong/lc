#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (26.62%)
# Total Accepted:    87.1K
# Total Submissions: 327.3K
# Testcase Example:  '[1]\n0'
#
# 
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
# 
# 
# 
# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
# 
# 
# 
# Example 2:
# coins = [2], amount = 3
# return -1.
# 
# 
# 
# Note:
# You may assume that you have an infinite number of each kind of coin.
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def coinChange(self, coins, amount):
        # 5 star, no idea, https://discuss.leetcode.com/topic/32743/clean-dp-python-code
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in xrange(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == MAX]
