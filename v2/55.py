





class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 6 star, no idea. 维护一个step变量，不断向前推进
        step = nums[0]
        for i in range(1, len(nums)):
            if step > 0:
                step -= 1
                step = max(nums[i], step) # 在当前索引上可以前进的步数
            else:
                return False
        return True