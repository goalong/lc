


class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 2 star, 直接从头到尾遍历
        length = len(nums)
        if length == 1:
            return 0
        for i in range(length):
            if i == 0:
                if nums[i] > nums[i+1]:
                    return i
            elif i == length - 1:
                if nums[i] > nums[i-1]:
                    return i
            else:
                if nums[i] > nums[i+1] and nums[i] > nums[i-1]:
                    return i



