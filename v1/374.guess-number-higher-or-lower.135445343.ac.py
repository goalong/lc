#
# [374] Guess Number Higher or Lower
#
# https://leetcode.com/problems/guess-number-higher-or-lower/description/
#
# algorithms
# Easy (36.49%)
# Total Accepted:    67.9K
# Total Submissions: 186.2K
# Testcase Example:  '10\n6'
#
# We are playing the Guess Game. The game is as follows: 
# 
# I pick a number from 1 to n. You have to guess which number I picked.
# 
# Every time you guess wrong, I'll tell you whether the number is higher or
# lower.
# 
# You call a pre-defined API guess(int num) which returns 3 possible results
# (-1, 1, or 0):
# 
# -1 : My number is lower
# ⁠1 : My number is higher
# ⁠0 : Congrats! You got it!
# 
# 
# Example:
# 
# n = 10, I pick 6.
# 
# Return 6.
# 
# 
#
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low <= high:
            middle = (low+high)//2
            rs = guess(middle)
            if rs == -1:
                high = middle - 1
            elif rs == 1:
                low = middle + 1
            else:
                return middle

        
