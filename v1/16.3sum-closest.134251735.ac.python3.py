#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (31.61%)
# Total Accepted:    165.3K
# Total Submissions: 523.1K
# Testcase Example:  '[0,0,0]\n1'
#
# Given an array S of n integers, find three integers in S such that the sum is
# closest to a given number, target. Return the sum of the three integers. You
# may assume that each input would have exactly one solution.
# 
# 
# ⁠   For example, given array S = {-1 2 1 -4}, and target = 1.
# 
# ⁠   The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
#
class Solution:
    def threeSumClosest(self, num, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 5 star.
        num.sort()
        rs = sum(num[:3])

        for i in range(len(num) - 2):
            low = i + 1
            high = len(num) - 1
            while low < high:
                total = num[i] + num[low] + num[high]
                if abs(target - total) < abs(target - rs):
                    rs = total
                if total < target:
                    low += 1
                elif total > target:
                    high -= 1
                else:
                    return target
        return rs

