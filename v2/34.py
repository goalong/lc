



class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 二分查找，注意边界条件
        low, high = 0, len(nums) - 1
        while low <= high:
            middle = (low+high)//2
            if target > nums[middle]:
                low = middle + 1
            elif target < nums[middle]:
                high = middle - 1
            else:
                start = end = middle
                while start > 0 and nums[start-1] == target:
                    start -= 1
                while end+1 < len(nums) and nums[end+1] == target:
                    end += 1
                return [start, end]
        return [-1, -1]


# Solution().searchRange([5,7,7,8,8,10], 8)