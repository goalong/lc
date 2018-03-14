






class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 6 star, dfs
        nums.sort()
        rs = []
        self.dfs(nums, [], rs)
        return rs

    def dfs(self, nums, path, rs):
        if nums == []:
            rs.append(path)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], rs)


# print(Solution().permuteUnique([1,1,2]))