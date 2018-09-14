class Solution(object):
    #  2 star, 使用字典，遍历数组时记录值到索引的映射
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        memo = {}
        for index, num in enumerate(nums):
            if target - num in memo:
                return [memo[target-num], index]
            memo[num] = index
        
