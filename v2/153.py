


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 5 star
        # 二分法的思路， 但实现有点麻烦
        # 即使旋转过了也会一半的任何一个元素始终比另一半的任何一个元素大，
        # 所以如果nums[mid] < nums[high]，说明最小元素一定在[left, mid]中，所以令high = mid；
        # 否则一定在[mid + 1, high]中，令low = mid + 1
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) / 2
            if nums[mid] <= nums[high]:  # min位于左侧上升沿
                high = mid
            else:  # min位于左侧上升沿与右侧上升沿之间
                low = mid + 1
        return nums[low]

# print(Solution().findMin([1, 2]))

