


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 6 star, 不能排序呢
        # todo, 堆排序
        if not nums:
            return 0
        from heapq import *
        heap = []
        for i in range(len(nums)):
            heappush(heap,nums[i])
            if len(heap) > k:
                heappop(heap)
        return heap[-1]