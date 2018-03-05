#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (29.02%)
# Total Accepted:    142.9K
# Total Submissions: 492.3K
# Testcase Example:  '[1,2,3]'
#
# 
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# 
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
# 
# 
# The replacement must be in-place, do not allocate extra memory.
# 
# 
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 5 star.
        if nums == sorted(nums, reverse=True):
            nums.sort()
            return
        for i in range(len(nums) -2, -1, -1):
            right = sorted(nums[i:], reverse=True)
            if nums[i:] != sorted(nums[i:], reverse=True):
                index = right.index(nums[i]) - 1
                start = right.pop(index)
                right.sort()
                nums[i:] =  [start] + right
                break
