class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        index = 0
        while True:
            for s in strs:
                if len(s) <= index or s[index] != strs[0][index]:
                    return strs[0][:index]
            index += 1


# s = Solution()
# print s.longestCommonPrefix(['abc', 'abccd'])