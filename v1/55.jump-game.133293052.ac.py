#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (29.57%)
# Total Accepted:    156.1K
# Total Submissions: 527.8K
# Testcase Example:  '[2,3,1,1,4]'
#
# 
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# 
# Each element in the array represents your maximum jump length at that
# position. 
# 
# 
# Determine if you are able to reach the last index.
# 
# 
# 
# For example:
# A = [2,3,1,1,4], return true.
# 
# 
# A = [3,2,1,0,4], return false.
# 
#
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 5 star. 
        step = nums[0]
        for i in range(1, len(nums)):
            if step > 0:
                step -= 1
                step = max(step, nums[i])
            else:
                return False
        return True
