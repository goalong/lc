




class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 3 star, 将字符串中数字或字母提取出来放到列表，对列表翻转，翻转后与原来相同则是回文
        if not s:
            return True
        s_list = [i for i in s.strip().lower() if i.isalnum()] # 先将字符串排除掉字母及数字之外的部分，然后对它们取小写形式
        reverse_s_list = s_list[::-1]
        if s_list == reverse_s_list:
            return True
        return False

# print(Solution().isPalindrome(" "))
