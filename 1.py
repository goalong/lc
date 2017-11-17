class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        memo = {}
        for index, i in enumerate(nums):
        	if target - i in memo:
        		return [memo[target-i], index]
        	memo[i] = index

print(Solution().twoSum([2,7, 11, 15], 9))
        
