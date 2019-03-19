class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 4 star，做出来了，首先假定第一个数字就是Majority Element，
        # 并且将它的count记为1，到后面如果遇到相同的数字，则将count加1，否则减1，
        # 减到0的时候需要变换当前的数字为Majority Element，重复该过程，最后剩下的就是要求的数字
        m = nums[0]
        count = 1
        for num in nums[1:]:
            if num == m:
                count += 1
            else:
                count -= 1
                if count == 0:
                    m = num
                    count = 1
        return m