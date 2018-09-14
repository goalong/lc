



class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 4 star, 不断比较当前数字的首位和末位，如果一样则去除首尾两个数字，继续比较剩下部分的首位和末位
        # 重点在如何得到一个数字的左边和右边的数
        if x < 0:
            return False
        div = 1
        while x / div >= 10:
            div *= 10
        while x > 0:
            left = x // div
            right = x % 10
            if left != right:
                return False
            x %= div
            x //= 10
            div //= 100
        return True

# if __name__ == "__main__":
#     assert Solution().isPalindrome(123) == False
#     assert Solution().isPalindrome(1) == True