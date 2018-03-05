#
# [80] Remove Duplicates from Sorted Array II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
#
# algorithms
# Medium (36.72%)
# Total Accepted:    143.2K
# Total Submissions: 389.9K
# Testcase Example:  '[]'
#
# 
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# 
# 
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
# 
# 
# Your function should return length = 5, with the first five elements of nums
# being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new
# length.
# 
#
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 5 star.
        if len(nums) < 3:
            return len(nums)
        count = 1
        cur_count = 1
        slow = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[slow]:
                nums[slow+1], nums[i] = nums[i], nums[slow+1]
                slow += 1
                count += 1
                cur_count = 1
            elif nums[i] == nums[slow] and cur_count < 2:
                cur_count += 1
                nums[slow + 1], nums[i] = nums[i], nums[slow + 1]
                slow += 1
                count += 1
            else:
                pass
        return count 
