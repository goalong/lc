


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 5 star, 必须掌握
        # 变量rs代表可能的占超过一半的数字，count是该数字出现的次数，遍历数组，
        # 如果count=0,  则用当前数字作为rs, 如果当前数字和rs相等，则count加1，不等则count减1
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

