#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (36.49%)
# Total Accepted:    180.7K
# Total Submissions: 495.3K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 
# 
# 
# Given an integer n, generate the nth term of the count-and-say sequence.
# 
# 
# 
# Note: Each term of the sequence of integers will be represented as a
# string.
# 
# 
# Example 1:
# 
# Input: 1
# Output: "1"
# 
# 
# 
# Example 2:
# 
# Input: 4
# Output: "1211"
# 
# 
#

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 3 star, 回头看
        result = "1"
        for _ in range(1, n):
            result = self.get_result(result)
        return result

    def get_result(self, s):
        index = 0
        rs = ''
        while index < len(s):
            times = 0
            char = s[index]
            while index < len(s) and s[index] == char:
                times += 1
                index += 1
            rs += str(times) + char
        return rs

# s = Solution()
# print(s.get_result("1211"))
# print(s.countAndSay(5))

