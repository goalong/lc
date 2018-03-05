#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (26.62%)
# Total Accepted:    132K
# Total Submissions: 496K
# Testcase Example:  '[-2]'
#
# 
# Find the contiguous subarray within an array (containing at least one number)
# which has the largest product.
# 
# 
# 
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
# 
#
class Solution(object):
    def maxProduct(self, nums):   # 4 star, no idea.
        """
        :type nums: List[int]
        :rtype: int
        """
        _max = small = big = nums[0]
        for i in nums[1:]:
            big, small = max(i, i * big, i*small), min(i, i*big, i*small)
            _max = max(big, _max)
        return _max
        
