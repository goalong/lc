#
# [260] Single Number III
#
# https://leetcode.com/problems/single-number-iii/description/
#
# algorithms
# Medium (52.95%)
# Total Accepted:    79K
# Total Submissions: 149.2K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# 
# Given an array of numbers nums, in which exactly two elements appear only
# once and all the other elements appear exactly twice. Find the two elements
# that appear only once.
# 
# 
# For example:
# 
# 
# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
# 
# 
# Note:
# 
# The order of the result is not important. So in the above example, [5, 3] is
# also correct.
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant space complexity?
# 
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 2 star.
        nums.sort()
        n = len(nums)
        index = 0
        rs = []
        while index < n:
            if index + 1 < n and nums[index] == nums[index+1]:
                index += 2
            elif index + 1 < n and nums[index] != nums[index+1]:
                if index + 2 < n and nums[index+1] == nums[index+2]:
                    rs.append(nums[index])
                    index += 3
                else:
                    rs = nums[index: index+2]
                    break
            else:
                rs.append(nums[index])
                index += 1
        return rs
