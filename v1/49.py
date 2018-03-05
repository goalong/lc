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
