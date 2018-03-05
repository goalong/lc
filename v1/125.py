class Solution(object):
    def isPalindrome(self, s):  # 1 star.
        """
        :type s: str
        :rtype: bool
        """
        if not s:
        	return True
        new_s = [i for i in s.lower().strip() if i.isalnum()]

        if new_s[::-1] == new_s:
        	return True
        return False
        
# s = Solution()
# print(s.isPalindrome('Abne'))