class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 4 star, 求最大值，考虑动态规划 设 f(n) 为从第 1 个数到第 n 个数的最大和，则递推公式为：
        # f(n) = max(nums[n] + f(n - 2), f(n - 1))
        if not nums:
            return 0
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        return dp[-1]