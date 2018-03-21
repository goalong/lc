




class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # 二分查找的变形 6 star, 边界条件比较难以考虑周全
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left+right)//2
            if nums[middle] == target:
                return True
            if nums[middle] == nums[left] == nums[right]: # 注意这个条件
                left += 1
                right -= 1
            elif nums[middle] >= nums[left]:
                if target < nums[middle] and target >= nums[left]:  # 注意target和两边都进行了比较
                    right = middle - 1
                else:
                    left = middle + 1
            elif nums[right] >= nums[middle]:
                if target > nums[middle] and target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return False

