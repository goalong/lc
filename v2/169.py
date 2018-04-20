


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 5 star, 必须掌握
        count = 0
        rs = None
        for num in nums:
            if count == 0:
                rs = num
            if num == rs:
                count += 1
            else:
                count -= 1
        return rs

