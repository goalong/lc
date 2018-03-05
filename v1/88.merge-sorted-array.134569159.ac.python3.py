#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (32.16%)
# Total Accepted:    220.4K
# Total Submissions: 685.2K
# Testcase Example:  '[1]\n1\n[]\n0'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# 
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2. The number of elements
# initialized in nums1 and nums2 are m and n respectively.
#
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # 5 star, 写错了N多次，重点注意。
        index = m +n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[index] = nums1[m]
                m -= 1
            else:
                nums1[index] = nums2[n]
                n -= 1
            index -= 1
        if m < 0:
            nums1[:n+1] = nums2[:n+1]


