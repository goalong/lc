#
# [65] Valid Number
#
# https://leetcode.com/problems/valid-number/description/
#
# algorithms
# Hard (12.94%)
# Total Accepted:    81.7K
# Total Submissions: 631.4K
# Testcase Example:  '"3"'
#
# Validate if a given string is numeric.
# 
# 
# Some examples:
# "0" => true
# "   0.1  " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# 
# 
# Note: It is intended for the problem statement to be ambiguous. You should
# gather all requirements up front before implementing one.
# 
# 
# 
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your
# function signature accepts a const char * argument, please click the reload
# button  to reset your code definition.
# 
#
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try: 
        	float(s)
        	return True
        except:
        	return False
        

