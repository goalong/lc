#
# [451] Sort Characters By Frequency
#
# https://leetcode.com/problems/sort-characters-by-frequency/description/
#
# algorithms
# Medium (51.59%)
# Total Accepted:    48.1K
# Total Submissions: 93.3K
# Testcase Example:  '"tree"'
#
# Given a string, sort it in decreasing order based on the frequency of
# characters.
# 
# Example 1:
# 
# Input:
# "tree"
# 
# Output:
# "eert"
# 
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
# answer.
# 
# 
# 
# Example 2:
# 
# Input:
# "cccaaa"
# 
# Output:
# "cccaaa"
# 
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# 
# 
# 
# Example 3:
# 
# Input:
# "Aabb"
# 
# Output:
# "bbAa"
# 
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
# 
# 
#
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 2 star.
        memo = {}
        for index, char in enumerate(s):
            memo[char] = memo.get(char, 0) + 1
        items = memo.items()
        l = sorted(items, key=lambda x: x[1], reverse=True)
        return  "".join([char*times for char, times in l])

