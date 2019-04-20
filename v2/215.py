
from heapq import *
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 6 star, 获取第k大的数，可以使用堆排序，对数组的前k个数维护一个长度为k的最小堆，然后
        # 对后面的数，如果小于最小堆的根，则跳过，大于则往堆上插入，并出堆一个，这样循环到最后，
        # 堆的根节点就是第k大的了
        heap = nums[:k]
        heapify(heap)
        for i in nums[k:]:
            if i < heap[0]:
                continue
            else:
                heappush(heap, i)
                heappop(heap)
        return heap[0]





