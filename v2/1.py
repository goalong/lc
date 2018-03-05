class Solution(object):
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
        
