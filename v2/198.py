


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 5 star, pass, 已掌握，求最大值，考虑动态规划，状态转移方程为 dp[x] = max(dp[x-1], nums[x] + dp[x-2])
        # dp[x] 表示从下标0到下标x 所能获取的价值的最大值，从第二个开始不断往后递推
        num_count = len(nums)
        if num_count < 3:
            return max(nums) if nums else 0
        dp = [0] * num_count
        dp[0], dp[1] = nums[0], nums[1]
        for i in range(1, num_count):  # 注意这里从第二个数开始就是采取动态规划来计算该位置上的最大和
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[-1]


# print(Solution().rob([2,1,1,2]))