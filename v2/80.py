







class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 6 star, 有点类似双指针，一前一后，后边的保存想要的结果，前边的向前遍历，记录每个数字出现的次数，次数大于2就直接忽略了
        # 前边的继续前进，次数小于等于2则将其放在j+1的索引上，并将j前进一位
        if len(nums) < 3:
            return len(nums)
        count = 1
        j = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[j]:
                if count == 2:
                    pass
                else:
                    count += 1
                    nums[j+1] = nums[i]
                    j += 1
            else:
                count = 1
                nums[j+1] = nums[i]
                j += 1
        return j + 1

# print(Solution().removeDuplicates([1,1,1, 1]))