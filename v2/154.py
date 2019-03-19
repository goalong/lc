class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 6 star, 没能解出来，前边思路同153，关键是处理相同的值的情况，这里使用了递归，非常巧妙
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                # 注意这里以mid+1为中间分开，使用mid会报错
                return min(self.findMin(nums[:mid + 1]), self.findMin(nums[mid + 1:]))
        return nums[left]
