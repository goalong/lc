class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 6 star,  没做出来
        # 遍历时记录一个当前最大值，一个当前最小值，因为最小值可能在一次负负得正时变成最大值，注意
        # 递推公式_max, _min = max(num, _min*num, _max*num), min(num, _min*num, _max*num)
        _min = _max = result = nums[0]
        for num in nums[1:]:
            _max, _min = max(num, _min * num, _max * num), min(num, _min * num, _max * num)
            result = max(_max, result)
        return result
