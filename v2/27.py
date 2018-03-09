


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 从头开始，每当有一个值不等于val, 将其放在数组对应索引上
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j


# print(Solution().removeElement([3, 2, 2, 3], 3))



