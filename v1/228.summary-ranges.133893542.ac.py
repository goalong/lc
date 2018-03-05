#
# [228] Summary Ranges
#
# https://leetcode.com/problems/summary-ranges/description/
#
# algorithms
# Medium (31.79%)
# Total Accepted:    95.4K
# Total Submissions: 300.1K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# 
# Given a sorted integer array without duplicates, return the summary of its
# ranges.
# 
# Example 1:
# 
# Input: [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# 
# 
# 
# Example 2:
# 
# Input: [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# 
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # 2 star
        if not nums:
            return []
        rs = [(str(nums[0]),)]
        i = 1
        left = nums[0]
        while i < len(nums):
            while i < len(nums) and nums[i] == nums[i-1] + 1:
                right = nums[i]
                i += 1
            else:
                right = nums[i-1]
            if left != right:
                rs[-1] = (str(left), str(right))
            if i < len(nums):
                left = nums[i]
                rs.append((str(left),))
                i += 1
        _r = []
        for i in rs:
            if len(i) == 2:
                _r.append("->".join(i))
            else:
                _r.append(i[0])
        return _r
