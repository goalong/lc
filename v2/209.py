class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # 7 star, 没能掌握，必须熟练掌握
        # 双指针，滑动窗口法
        # 双指针法，右指针不断往右遍历，如果左指针和右指针构成的子数组的和大于等于s了，左指针也开始往右遍历，意图寻找
        # 以右指针结尾且和大于等于s的子数组的最小长度，找到当前的最小长度左指针往前移动一步，右指针也继续往前直到和左指针构成的数组的和再次大于等于s,
        # 这时左指针又可以往前了，直到找到当前右指针为结尾的最小长度的子数组，一直这样重复，直到右指针到达数组的最右边
        if sum(nums) < s:
            return 0
        _min = 0xffffffff
        left, right = 0, 1
        cur = nums[0]
        while right < len(nums):
            while cur < s and right < len(nums):
                cur += nums[right]
                right += 1

            while cur >= s and left < right:
                cur -= nums[left]
                left += 1
            _min = min(_min, right - left + 1)
        return _min


print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))

# 一开始自己做的，超时了
# class Solution:
#     def minSubArrayLen(self, s, nums):
#         """
#         :type s: int
#         :type nums: List[int]
#         :rtype: int
#         """
#         _min = 0xffffffff
#         if sum(nums) < s:
#             return 0
#         length = len(nums)
#         for i in range(length):
#             for j in range(i + 1, length + 1):
#                 cur_sum = sum(nums[i:j])
#                 if cur_sum >= s:
#                     _min = min(_min, j - i)
#                     break
#         return _min
