



class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 3 star， 双指针，从索引0开始，快的指针遇到非0值，则将慢指针所在位置的值更新为快指针上的值，然后对慢指针加1
        fast = slow = 0
        length = len(nums)
        while fast < length:
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
            else:
                fast += 1
        nums[slow:] = [0] * (length - slow)

print(Solution().moveZeroes([0,1,0,2,3, 0]))