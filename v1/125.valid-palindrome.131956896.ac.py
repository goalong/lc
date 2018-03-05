#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (26.91%)
# Total Accepted:    212K
# Total Submissions: 787.8K
# Testcase Example:  '""'
#
# 
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# 
# 
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
# 
# 
# 
# Note:
# Have you consider that the string might be empty? This is a good question to
# ask during an interview.
# 
# For the purpose of this problem, we define empty string as valid palindrome.
# 
#
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
        	return True
        new_s = [i for i in s.lower().strip() if i.isalnum()]

        if new_s[::-1] == new_s:
        	return True
        return False
        
s = Solution()
print(s.isPalindrome('Abne'))
