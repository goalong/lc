#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (29.02%)
# Total Accepted:    142.9K
# Total Submissions: 492.3K
# Testcase Example:  '[1,2,3]'
#
# 
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# 
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
# 
# 
# The replacement must be in-place, do not allocate extra memory.
# 
# 
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 5 star. 需要在看 直到熟练. 从倒数第二个的位置开始向前遍历，每次考察当前位置及之后的数字组成的子列表是否是倒序排列的，
        # 如果是倒序排列的，则继续往前遍历；如果不是，说明可以调整位置得到想要的子列表, 调整的方法是将当前位置的数字在倒序排列
        # 中的索引减去1得到这个子列表的起始，子列表后面的部分是除起始数字外剩余部分的正序排列
        if nums == sorted(nums, reverse=True):
            nums.sort()
            return
        for i in range(len(nums) -2, -1, -1):
            right = sorted(nums[i:], reverse=True)
            if nums[i:] != right:
                index = right.index(nums[i]) - 1
                start = right.pop(index)
                right.sort()
                nums[i:] =  [start] + right
                break

nums = [1, 2, 3, 5, 6, 4]
Solution().nextPermutation(nums)