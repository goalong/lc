






class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 5 star, 计数排序，先计算每个颜色的数量，然后逐个往原来的数组填充直到达到数量
        count = [0] * 3
        for i in nums:
            count[i] += 1
        index = 0
        for i in range(3):
            for j in range(count[i]):
                nums[index] = i
                index += 1