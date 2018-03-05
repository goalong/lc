#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (31.77%)
# Total Accepted:    184.7K
# Total Submissions: 581.4K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# 
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
# 
#
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # 3 star.
        intervals.sort(key=lambda x:x.start)
        rs = []
        for i in intervals:
            if not rs:
                rs.append(i)
            else:
                last = rs[-1]
                if i.start > last.end:
                    rs.append(i)
                else:
                    last.end = max(last.end, i.end)
        return rs
