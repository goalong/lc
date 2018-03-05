class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 中文测试
        index = -1
        needle_len = len(needle)
        for i in range(len(haystack) - needle_len + 1):
        	if haystack[i:i+needle_len] == needle:
        		index = i
        		break
        return index
        


print(Solution().strStr('abder', 'r'))