#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (36.19%)
# Total Accepted:    218.9K
# Total Submissions: 604.9K
# Testcase Example:  '""'
#
# Given a digit string, return all possible letter combinations that the number
# could represent.
# 
# 
# 
# A mapping of digit to letters (just like on the telephone buttons) is given
# below.
# 
# 
# 
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# 
# Note:
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
# 
#
class Solution(object):
    def letterCombinations(self, digits):   # todo, no idea, should master dfs
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'1': [],
        		'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                }
        if not digits:
        	return []
        rs = []
        self.dfs(digits, '', d, rs)
        return rs
    def dfs(self, digits, current, d, rs):
    	if not digits:
    		rs.append(current)
    		return 
    	for i in d[digits[0]]:
    		self.dfs(digits[1:], current + i, d, rs)




# s = Solution()
# print s.letterCombinations('')
