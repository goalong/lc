

# 给定一个数组和一个窗口大小K，要你从数组中按顺序将所有相邻的K个数中最大值输出。
# 复杂度O(n)
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 滑动窗口， 7 star, 面试遇到，当时想的是暴力的解法
        # 维护一个双向队列，其保持递减顺序，若队列头位置不在窗口中，队列头出队列，当前数小于队列尾或队列为空，则队列尾出队列，进行循环操作后，加入当前项。队列头即使当前窗口中的最大值。
        if not nums:
            return []
        if len(nums) < k:
            return [max(nums)]
        queue = []
        ret = []
        for i in range(len(nums)):
            while queue and queue[0] <= i - k:
                queue.pop(0)
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                ret.append(nums[queue[0]])
        return ret

print(Solution().maxSlidingWindow([7,2,4], 2))