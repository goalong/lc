#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (31.97%)
# Total Accepted:    110.3K
# Total Submissions: 345.1K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
# one, return 0 instead.
# 
# 
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
# 
# 
# click to show more practice.
# 
# More practice:
# 
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n).
# 
# 
# Credits:Special thanks to @Freezen for adding this problem and creating all
# test cases.
#
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # 5 star. idea: http://bookshadow.com/weblog/2015/05/12/leetcode-minimum-size-subarray-sum/
        start, end, total = 0, 0, 0
        _len = len(nums)
        rs = _len + 1
        while end < _len:
            while total < s and end < _len:
                total += nums[end]
                end += 1
            while total >= s and  start < end:
                rs = min(rs, end - start)
                total -= nums[start]
                start += 1
        return 0 if rs == _len + 1 else rs
