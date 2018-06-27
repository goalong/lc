


class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # 5 star, dfs
        rs = []
        self.dfs(k, n, rs, 1, [])
        return rs

    def dfs(self, k, n, rs, start, path):
        if k == 0 and n == 0:
            rs.append(path)
            return
        for i in range(start, 10):
            self.dfs(k-1, n-i, rs, i+1, path + [i])

# print(Solution().combinationSum3(3, 9))