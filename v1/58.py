class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split(' ')
        for i in range(len(s) - 1, -1, -1):
            if s[i]:
                return len(s[i])
        return 0


# print(Solution().lengthOfLastWord('a b c e h  '))
        
