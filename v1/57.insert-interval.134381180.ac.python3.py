#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Hard (28.85%)
# Total Accepted:    120.6K
# Total Submissions: 418.1K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
# 
# You may assume that the intervals were initially sorted according to their
# start times.
# 
# 
# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
# 
# 
# 
# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as
# [1,2],[3,10],[12,16].
# 
# 
# 
# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
# 
#
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # 5 star. 不难，但是很多边界条件需要考虑。
        if not intervals:
            return [newInterval]
        new_index = 0
        if newInterval.start < intervals[0].start:
            intervals.insert(0, newInterval)
            new_index = 0
        elif newInterval.start >= intervals[-1].start:
            intervals.append(newInterval)
            new_index = len(intervals) - 1
        else:
            for index, interval in enumerate(intervals):
                if index + 1 < len(intervals) and newInterval.start >= interval.start and newInterval.start < intervals[index+1].start:
                    intervals.insert(index+1, newInterval)
                    new_index = index+1
                    break
        index = max(0, new_index - 1)
        if index + 1 < len(intervals):
            if intervals[index].end >= intervals[index+1].start >= intervals[index].start:
                intervals[index].end = max(intervals[index].end, intervals[index+1].end)
                while index < len(intervals) - 1:
                    if intervals[index+1].start <= intervals[index].end:
                        intervals[index].end = max(intervals[index].end, intervals[index + 1].end)
                        intervals.pop(index+1)
                    else:
                        break
            else:
                if index + 2 < len(intervals):
                    if intervals[index+1].end >= intervals[index + 2].start >= intervals[index+1].start:
                        intervals[index+1].end = max(intervals[index+1].end, intervals[index + 2].end)
                        index += 1
                        while index < len(intervals) - 1:
                            if intervals[index + 1].start <= intervals[index].end:
                                intervals[index].end = max(intervals[index].end, intervals[index + 1].end)
                                intervals.pop(index + 1)
                            else:
                                break

        return intervals

