#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (32.45%)
# Total Accepted:    110.6K
# Total Submissions: 340.7K
# Testcase Example:  '""\n""'
#
# 
# Given two words word1 and word2, find the minimum number of steps required to
# convert word1 to word2. (each operation is counted as 1 step.)
# 
# 
# 
# You have the following 3 operations permitted on a word:
# 
# 
# 
# a) Insert a character
# b) Delete a character
# c) Replace a character
# 
#
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #
        len1 = len(word1)
        len2 = len(word2)
        # initialization
        dp = [ [0 for j in xrange(len2 + 1)] for i in xrange(len1 + 1) ]
        for i in xrange(len1 + 1):
            dp[i][0] = i
        for j in xrange(len2 + 1):
            dp[0][j] = j
        # dp
        for i in xrange(1, len1 + 1):
            for j in xrange(1, len2 + 1):
                dp[i][j] = dp[i-1][j-1] if word1[i-1] == word2[j-1] else min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[len1][len2]
        
