#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (49.52%)
# Total Accepted:    95.7K
# Total Submissions: 193.1K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# 
# Given a non-empty array of integers, return the k most frequent elements.
# 
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
# 
# 
# Note: 
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
# 
#
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        memo = {}
        for num in nums:
            memo[num] = memo.get(num, 0) + 1
        items = memo.items()
        l = sorted(items, key=lambda x: x[1], reverse=True)[:k]
        return [k for k, v in l]
