





class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 6 star, dfs, 多练习
        nums.sort()
        rs = []
        self.dfs([], rs, 0, nums)
        return rs


    def dfs(self, path, rs, start, nums):
        if len(path) <= len(nums) and path not in rs:
            rs.append(path)
        for i in range(start, len(nums)):
            self.dfs(path+[nums[i]], rs, i+1, nums)

# print(Solution().subsetsWithDup([1,2,2]))