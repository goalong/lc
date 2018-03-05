#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (35.69%)
# Total Accepted:    303.6K
# Total Submissions: 850.8K
# Testcase Example:  '-2147483648'
#
# Determine whether an integer is a palindrome. Do this without extra space.
# 
# click to show spoilers.
# 
# Some hints:
# 
# Could negative integers be palindromes? (ie, -1)
# 
# If you are thinking of converting the integer to string, note the restriction
# of using extra space.
# 
# You could also try reversing an integer. However, if you have solved the
# problem "Reverse Integer", you know that the reversed integer might overflow.
# How would you handle such case?
# 
# There is a more generic way of solving this problem.
# 
# 
#
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 6 star. must master.
        if x < 0:
            return False
        div = 1
        while x / div >= 10:
            div *= 10
        while x > 0:
            l = x // div
            r = x % 10
            if l != r:
                return False
            x %= div
            x //=10
            div //=100
        return True
        
