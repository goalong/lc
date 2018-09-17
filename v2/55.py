





class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 6 star, no idea. 维护一个step变量，不断向前推进, 每个位置上可前进的最大步数等于前面剩余的步数和nums[i]中较大的一个数值
        step = nums[0]
        for i in range(1, len(nums)):
            if step > 0:
                step -= 1
                step = max(nums[i], step) # 在当前索引上可以前进的步数
            else:
                return False
        return True