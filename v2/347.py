
# Top K Frequent Elements
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 6 star, 使用一个字典记录每个数字出现的次数，然后对字典按值排序(注意如果次数相同的，排序函数会按照元素从小到大的顺序排列的)
        # 然后对排序的结果取前k个就行了，因为使用了排序，时间复杂度O(nlogn)
        count_map = {}
        for num in nums:
            count_map[num] = count_map[num] + 1 if num in count_map else 1
        sorted_data = sorted(count_map.items(), key=lambda x: x[1], reverse=True)
        return [sorted_data[i][0] for i in range(k)]

class Solution2(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 桶排序，也很巧妙，需要熟悉一下桶排序
        data, res = {}, []
        for i in nums:
            data[i] = data[i] + 1 if i in data else 1
        # 桶的索引表示元素的个数，索引上的列表表示有此个数的元素
        bucket = [[] for i in range(len(nums)+1)]
        for key in data:
            print(key, data[key])
            bucket[data[key]].append(key)
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i]:
                res.extend(bucket[i])
            if len(res) >= k:
                break
        return res[:k]

from collections import Counter
from heapq import *
class Solution3(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 7 star, 面试遇到过，需要重视
        counts = Counter(nums)
        heap = [(-count, num) for num, count in counts.items()]
        heapify(heap)
        return [heappop(heap)[1] for _ in range(k)]

