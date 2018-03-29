






class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 5 star, 位操作需要补上，这一块太弱了
        # 一个数和自己的异或是0，和0的异或是自己
        rs = nums[0]
        for i in range(1, len(nums)):
            rs = rs ^ nums[i]
        return rs
