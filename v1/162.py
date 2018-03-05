class Solution(object):
    def findPeakElement(self, nums):   # 1 star.
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        i = 0
        while i <= n - 1:
            if i == 0:
                if nums[i] > nums[i+1]:
                    return i
            elif i == n-1:
                if nums[i] > nums[i-1]:
                    return i
            else:
                if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                    return i
            i += 1