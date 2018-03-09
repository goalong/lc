


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # todo, 需要加深理解，还不能很顺利的做出
        if not nums:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                nums[j+1], nums[i] = nums[i], nums[j+1]
                j += 1
        return j + 1


Solution().removeDuplicates([1,2,3])