


class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 6 star, 没做出来
        # 从第二个开始，每次记录最大值和最小值，因为最小值乘以一个负数也可能是最大值
        _max = small = big =  nums[0]
        for i in nums[1:]:
            # small和big的递推公式
            small, big = min(i, i*big, i*small), max(i, i*big, i*small)
            _max = max(_max, big)
        return _max

