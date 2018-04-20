


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 2 star, 两边往中间夹逼，注意没法用二分法
        left, right = 0, len(numbers) - 1
        while left <= right:
            total = numbers[right] + numbers[left]
            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                return [left+1, right+1]
