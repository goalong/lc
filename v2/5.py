




class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rs = ""
        for index, char in enumerate(s):
        	rs = max(self.get_len(s,index, index), self.get_len(s, index, index+1), rs, key=len)
        return rs

    # 这个解法非常巧妙， 从一个字符向左右扩展，直到左右不相等
    def get_len(self, s, l, r):
    	while l >= 0 and r < len(s) and s[l] == s[r]:
    		l -= 1
    		r += 1
    	return s[l+1:r]
