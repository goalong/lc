class Solution(object):
    def reverseWords(self, s):   # 1 star
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])


s = Solution()
print(s.reverseWords('the sky is blue'))