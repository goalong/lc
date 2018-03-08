




class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        rs = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] > nums[i-1]:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    total = nums[i] + nums[left] + nums[right]
                    if abs(target - total) < abs(target - rs):
                        rs = total
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        return total
        return rs
