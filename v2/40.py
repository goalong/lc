






class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 5 star, dfs
        candidates.sort()
        rs = []
        self.dfs(0, candidates, [], rs, target)
        return rs

    def dfs(self, current_sum, candidates, path, rs, target):
        if current_sum == target:
            rs.append(path)
            return
        elif current_sum > target:
            return
        else:
            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i-1]:
                    continue
                if current_sum + candidates[i] > target:
                    break
                self.dfs(current_sum+candidates[i], candidates[i+1:], path+[candidates[i]], rs, target)
