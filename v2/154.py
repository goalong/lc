


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 6 star, 二分法，但不好处理，思路同153，只是加上对相等元素的处理
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low+high)//2
            if nums[high] > nums[mid]:
                high = mid
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                return min(self.findMin(nums[:mid+1]), self.findMin(nums[mid+1:]))
        return nums[low]

# print(Solution().findMin([1, 1]))