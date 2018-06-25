#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (47.81%)
# Total Accepted:    247.1K
# Total Submissions: 516.8K
# Testcase Example:  '[1]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 5 star. 非常巧妙，想不出来呀
        # 变量count标记可能数字的次数
        count, rs = 0, None
        for num in nums:
            if count == 0:
                rs = num
            if num == rs:
                count += 1
            else:
                count -= 1
        return rs
        
