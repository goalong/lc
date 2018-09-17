


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # todo, 需要加深理解，还不能很顺利的做出
        # 5 star, 双指针法，后面的指针只有在前边的指针遇到了新的数值时才向前移动
        if not nums:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                nums[j+1], nums[i] = nums[i], nums[j+1]
                j += 1
        return j + 1


Solution().removeDuplicates([1,2,3])