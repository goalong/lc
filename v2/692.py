

from heapq import *
import collections
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # 7 star, 使用heap时注意它是最小堆，以及需要的返回顺序，由于是最小堆，对相同的数字和字符串是按升序排列的
        # 这个题自己做时就因为相同频率的字符返回的顺序不符合要求而做错了
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapify(heap)
        return [heappop(heap)[1] for _ in range(k)]
