




class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 6 star, dfs， 要熟练
        rs = []
        self.dfs(nums, [], rs)
        return rs

    def dfs(self, nums, path, rs):
        if nums == []:
            rs.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], rs)

# print(Solution().permute([1,2,3]))
