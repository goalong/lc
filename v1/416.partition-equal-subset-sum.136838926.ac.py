#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (38.98%)
# Total Accepted:    38.9K
# Total Submissions: 99.8K
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array containing only positive integers, find if the array
# can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.
# 
# 
# Note:
# 
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# 
# 
# 
# Example 1:
# 
# Input: [1, 5, 11, 5]
# 
# Output: true
# 
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# 
# 
# 
# Example 2:
# 
# Input: [1, 2, 3, 5]
# 
# Output: false
# 
# Explanation: The array cannot be partitioned into equal sum subsets.
# 
# 
#
class Solution(object):
    def canPartition(self, nums):
        # 6 star.
        nums.sort(reverse=True)
        half = sum(nums)//2
        def helper(start, target):
            if target < 0:
                return
            elif target == 0:
                return True
            for i in range(start, len(nums)):
                if nums[i] > half:
                    return False
                if helper(i+1, target-nums[i]):
                    return True
            return False

        return False if sum(nums)%2 else helper(0, half)


