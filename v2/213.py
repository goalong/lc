
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 6 star, 动态规划，分包含和不包含第一个两种情况
        # dp[x] = max(dp[x-1], dp[x-2] + nums[x])
        # todo, 重写一下，构造一个函数来处理
        if not nums:
            return 0
        length = len(nums)
        if length <= 3:
            return max(nums)
        dp0 = [0] * (length - 1)
        dp0[0] = nums[0]
        dp0[1] = nums[1] if nums[1] > nums[0] else nums[0]
        for i in range(2, length - 1):
            dp0[i] = max(dp0[i - 1], dp0[i - 2] + nums[i])
        dp1 = [0] * (length - 1)
        dp1[0] = nums[1]
        dp1[1] = nums[2] if nums[2] > nums[1] else nums[1]
        for j in range(2, length - 1):
            dp1[j] = max(dp1[j - 1], dp1[j - 2] + nums[j+1])
        return max(dp0[-1], dp1[-1])
#
#
# print(Solution().rob([1,2,3,1]))
#
#

