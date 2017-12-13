class Solution(object):
    def findKthLargest(self, nums, k): # todo, this is easy, try to use heap later
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        return nums[k-1]
