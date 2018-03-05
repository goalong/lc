#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (37.93%)
# Total Accepted:    186K
# Total Submissions: 490.4K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# 
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
# Return:
# 
# [
# ⁠ ["ate", "eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note: All inputs will be in lower-case.
#
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        str_dict = {}
        for s in strs:
            sorted_s = tuple(sorted(s))
            if sorted_s in str_dict:
                str_dict[sorted_s].append(s)
            else:
                str_dict[sorted_s] = [s]
        return [i for i in str_dict.values()]


# s = Solution()
# print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

