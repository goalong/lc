




class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 4 star, 将字符串中数字或字母提取出来放到列表，对列表翻转，翻转后与原来相同则是回文
        if not s:
            return True
        s_list = [i for i in s.strip().lower() if i.isalnum()]
        reverse_s_list = s_list[::-1]
        if s_list == reverse_s_list:
            return True
        return False

# print(Solution().isPalindrome(" "))
