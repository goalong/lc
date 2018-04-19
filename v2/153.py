


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 5 star
        # 二分法的思路， 但实现有点麻烦
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) / 2
            if nums[mid] <= nums[high]:  # min位于左侧上升沿
                high = mid
            else:  # min位于左侧上升沿与右侧上升沿之间
                low = mid + 1
        return nums[low]

# print(Solution().findMin([1, 2]))

