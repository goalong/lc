class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 6 star, pass, 动态规划，首先因为是环形，可以将问题分成包含第一家和不包含第一家两种情况
        # 对每一种情况，都是回到了跟House Robber一样的情形，
        # dp[i]表示以索引i结尾的能抢到的最大金额，状态转移方程： dp[i] = max(dp[i-1], dp[i-2]+nums[i]), 注意i=0和1时要特殊处理
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        return max(self.rob_helper(nums[:-1]), self.rob_helper(nums[1:]))

    def rob_helper(self, nums):
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

#
#
# print(Solution().rob([1,2,3,1]))
#
#

