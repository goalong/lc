


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 5 star, no idea
        # 动态规划，dp[i]代表以i结尾的最长的LIS，状态转移方程 dp[i] = max(dp[i], dp[j]+1), j是0到i之间的范围
        length = len(nums)
        if not nums:
            return 0
        dp = [1] * length
        for i in range(length):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

