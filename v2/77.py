




class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # 6 star, 起初用dfs做的，结果一直超时，
        # todo, 这个解法是别处看来的，需要自己再做
        if k > n:
            return []
        if k == 1:
            return [[i + 1] for i in range(n)]
        if n > k:
            result = [r + [n] for r in self.combine(n - 1, k - 1)] + self.combine(n - 1, k)  # 有n的 和 没n的
        else:
            result = [r + [n] for r in self.combine(n - 1, k - 1)]  # 之所以有这个else, 是处理n=k的
        return result

# print(Solution().combine(4, 2))