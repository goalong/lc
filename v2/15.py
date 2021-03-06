


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 4 star, 先排序，然后最外层一个遍历，将当且的数字和余下部分的首尾的数字之和与0做比较，如果比0小
        # 将左指针向前一位，比0大将右指针向后一位，等于0则加到结果集里
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

