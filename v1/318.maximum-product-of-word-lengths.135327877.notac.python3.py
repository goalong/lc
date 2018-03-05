#
# [318] Maximum Product of Word Lengths
#
# https://leetcode.com/problems/maximum-product-of-word-lengths/description/
#
# algorithms
# Medium (45.50%)
# Total Accepted:    60.3K
# Total Submissions: 132.5K
# Testcase Example:  '["abcw","baz","foo","bar","xtfn","abcdef"]'
#
# 
# ⁠   Given a string array words, find the maximum value of length(word[i]) *
# length(word[j]) where the two words do not share common letters.
# ⁠   You may assume that each word will contain only lower case letters.
# ⁠   If no such two words exist, return 0.
# 
# 
# 
# ⁠   Example 1:
# 
# 
# ⁠   Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
# ⁠   Return 16
# ⁠   The two words can be "abcw", "xtfn".
# 
# 
# ⁠   Example 2:
# 
# 
# ⁠   Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
# ⁠   Return 4
# ⁠   The two words can be "ab", "cd".
# 
# 
# ⁠   Example 3:
# 
# 
# ⁠   Given ["a", "aa", "aaa", "aaaa"]
# ⁠   Return 0
# ⁠   No such pair of words.    
# 
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#
class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=len)
        rs = 0
        n = len(words)
        for i in range(n-1, -1, -1):
            if len(words[i]) * len(words[i-1]) < rs:
                break
            for j in range(i-1, -1, -1):
                product = len(words[i])*len(words[j])
                if product < rs:
                    break
                if set(words[i])&set(words[j]) == set():
                    rs = product

        return rs
        
