#
# [187] Repeated DNA Sequences
#
# https://leetcode.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (32.85%)
# Total Accepted:    91.3K
# Total Submissions: 278K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# 
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to
# identify repeated sequences within the DNA.
# 
# Write a function to find all the 10-letter-long sequences (substrings) that
# occur more than once in a DNA molecule.
# 
# 
# For example,
# 
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
# 
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].
# 
#
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # 1 star.
        n = len(s)
        if n <= 10:
        	return []
        str_map = {}
        for i in range(n-10+2):
        	seq = s[i:i+10]
        	if seq in str_map:
        		str_map[seq] += 1
        	else:
        		str_map[seq] = 1
        return [i for i in str_map.keys() if str_map[i] > 1]

