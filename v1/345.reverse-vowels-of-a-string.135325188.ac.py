#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (39.07%)
# Total Accepted:    102.1K
# Total Submissions: 261.2K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
# 
# 
# Example 1:
# Given s = "hello", return "holle".
# 
# 
# 
# Example 2:
# Given s = "leetcode", return "leotcede".
# 
# 
# 
# Note:
# The vowels does not include the letter "y".
# 
#
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 3 star
        vowels = "aeiou"
        left, right = 0, len(s) - 1
        l = list(s)
        while left <= right:
            while left <= right and l[left].lower() not in vowels:
                left += 1
            while left <= right and l[right].lower() not in vowels:
                right -= 1
            if left <= right:
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1
        return "".join(l)
