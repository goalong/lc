


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 5 star, 二分法,
        # 这个是先比较左右两边和中间的大小，分类讨论来进行排除一半，然后比较中间的和目标数字
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left+right)//2
            if nums[middle] == target:
                return middle
            if nums[middle] >= nums[left]:
                if nums[middle] > target >= nums[left]:
                    right = middle - 1
                else:
                    left = middle + 1
            elif nums[right] > nums[middle]:
                if nums[right] >= target > nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1

Solution().search([3, 1], 1)
