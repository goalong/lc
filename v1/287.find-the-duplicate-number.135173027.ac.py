#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (44.20%)
# Total Accepted:    99.9K
# Total Submissions: 225.9K
# Testcase Example:  '[1,1]'
#
# 
# Given an array nums containing n + 1 integers where each integer is between 1
# and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
# 
# 
# 
# Note:
# 
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.
# 
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 6 star, idea: https://www.hrwhisper.me/leetcode-find-the-duplicate-number/
        # haven't understand the solution
        low, high = 1, len(nums) - 1
        while low <= high:
            middle = (low+high)//2
            count = sum([1 for i in nums if i <= middle])
            if count <= middle:
                low = middle + 1
            else:
                high = middle - 1
        return low

