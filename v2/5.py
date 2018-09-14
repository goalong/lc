




class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 5 star, 遍历字符串，计算以每个字符为中心的回文字符串的长度并比较
        rs = ""
        for index, char in enumerate(s):
            # 注意以一个字母为中心的回文有两种情况，例如aba和abba两个回文都以b为中心，但其长度一个奇数一个偶数
        	rs = max(self.get_len(s,index, index), self.get_len(s, index, index+1), rs, key=len)
        return rs

    # 这个解法非常巧妙， 从一个字符向左右扩展，直到左右不相等
    def get_len(self, s, l, r):
    	while l >= 0 and r < len(s) and s[l] == s[r]:
    		l -= 1
    		r += 1
    	return s[l+1:r]
