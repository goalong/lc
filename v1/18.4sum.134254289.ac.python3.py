#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (27.46%)
# Total Accepted:    148.3K
# Total Submissions: 540.1K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array S of n integers, are there elements a, b, c, and d in S such
# that a + b + c + d = target? Find all unique quadruplets in the array which
# gives the sum of target.
# 
# Note: The solution set must not contain duplicate quadruplets.
# 
# 
# 
# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
#
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 5 star. 
        nums.sort()
        rs = set()
        for i in range(len(nums) - 3):
            j = i + 1
            while j < (len(nums) - 2):
                low = j + 1
                high = len(nums) - 1
                while low < high:
                    total = nums[i] + nums[j] + nums[low] + nums[high]
                    if total < target:
                        low += 1
                    elif total > target:
                        high -= 1
                    else:
                        rs.add((nums[i], nums[j], nums[low], nums[high]))
                        low += 1
                j += 1
        return list(rs)
