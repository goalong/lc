#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (21.80%)
# Total Accepted:    299.7K
# Total Submissions: 1.4M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array S of n integers, are there elements a, b, c in S such that a +
# b + c = 0? Find all unique triplets in the array which gives the sum of
# zero.
# 
# Note: The solution set must not contain duplicate triplets.
# 
# 
# For example, given array S = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
#
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        # 6 star. 先排序，后面从两边逼近
        num.sort()
        rs = set()
        for i in range(len(num) - 2):
            if i == 0 or num[i] > num[i-1]:
                low = i + 1
                high = len(num) - 1
                while low < high:
                    total = num[i] + num[low] + num[high]
                    if  total < 0:
                        low += 1
                    elif total > 0:
                        high -= 1
                    else:
                        rs.add((num[i], num[low], num[high]))
                        low += 1
        return list(rs)
