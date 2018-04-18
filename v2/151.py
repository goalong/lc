
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 3 star
        return " ".join(s.split()[::-1])

print(Solution().reverseWords("abc"))
