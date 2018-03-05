#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (23.35%)
# Total Accepted:    89.8K
# Total Submissions: 384.6K
# Testcase Example:  '[1]'
#
# Given a list of non negative integers, arrange them such that they form the
# largest number.
# 
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
# 
# Note: The result may be very large, so you need to return a string instead of
# an integer.
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def compare(a, b):
            return int(b+a) - int(a+b)
        nums = sorted([str(i) for i in nums], cmp=compare)
        ans = ''.join(nums).lstrip('0')
        return ans or "0"
        
