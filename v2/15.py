


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        rs = set()
        for i in range(len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:  # 排除重复的数字
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    total = nums[i] + nums[left] + nums[right]
                    if total < 0:
                        left += 1
                    elif total > 0:
                        right -= 1
                    else:
                        rs.add((nums[i], nums[left], nums[right]))
                        left += 1
        return list(rs)

