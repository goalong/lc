class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 2 star.
        n = len(nums)
        nums[:k], nums[k:] = nums[n-k:], nums[:n-k]

s = Solution()
a = [1,2,3,4,5,6,7]
s.rotate(a, 3)
print(a)