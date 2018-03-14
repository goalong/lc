




class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 6 star, 思路很巧妙，必须掌握
        current_sum, max_sum = -0xffffffff, -0xffffffff
        for i in nums:
            if current_sum < 0:
                current_sum = i
            else:
                current_sum += i
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum


print(Solution().maxSubArray([1]))