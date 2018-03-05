#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (34.74%)
# Total Accepted:    151.3K
# Total Submissions: 435.4K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# 
# 
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
# 
# 
# 
# 
# For example,
# 
# Consider the following matrix:
# 
# 
# [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# 
# 
# Given target = 3, return true.
#
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 4 star. test case not easy to pass.
        if not matrix or not matrix[0]:
            return False
        last_nums = [row[-1] for row in matrix]
        low, high = 0, len(last_nums) - 1
        middle = (low + high) // 2
        if target > last_nums[-1] or target < matrix[0][0]:
            return False
        while low < high:
            middle = (low + high) // 2
            if last_nums[middle] > target:
                high = middle
            elif last_nums[middle] < target:
                low = middle + 1
            else:
                break
        else:
            middle = (low+high)//2
        middle = middle if last_nums[middle] >= target else middle - 1
        low, high = 0, len(matrix[0]) - 1
        while low < high:
            mid = (low + high) // 2
            if matrix[middle][mid] > target:
                high = mid
            elif matrix[middle][mid] < target:
                low = mid + 1
            else:
                return True
        else:
            if matrix[middle][low] == target:
                return True
        return False

