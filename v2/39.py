




class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 5 star, dfs, 先排序，以及如果当前组合的和大于目标值则后面的就不用继续了，可以省点时间
        rs = []
        candidates.sort()
        self.dfs(0, candidates, [], rs, target)
        return rs

    def dfs(self, current_sum, candidates, path, rs, target):
        if current_sum == target:
            rs.append(path)
        elif current_sum > target:
            return
        else:
            for i in range(len(candidates)):
                if current_sum+candidates[i] > target:
                    break
                self.dfs(current_sum+candidates[i], candidates[i:], path+[candidates[i]], rs, target)

# print(Solution().combinationSum([2,3,6,7], 7))