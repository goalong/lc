
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 5 star, no idea.
        # 对于位置i, 第一轮计算0到i-1位置的乘积，第二轮计算i+1到最后的乘积
        length = len(nums)
        rs = [1] * length
        cur = 1
        for i in range(length-1):
            cur = cur * nums[i]
            rs[i+1] = rs[i+1] * cur
        cur = 1
        for j in range(length-1, 0, -1):
            cur *= nums[j]
            rs[j-1] *= cur
        return rs
