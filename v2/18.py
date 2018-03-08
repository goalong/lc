



class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 思路同3sum, 分别对前两个遍历，后两个从两边逼近
        nums.sort()
        rs = set()
        for i in range(len(nums) - 3):
            j = i + 1
            while j < len(nums) - 2:
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total > target:
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        rs.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                j += 1
        return list(rs)

