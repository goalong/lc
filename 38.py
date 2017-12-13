
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"
        for _ in range(1, n):
            result = self.get_result(result)
        return result

    def get_result(self, s):
        index = 0
        rs = ''
        while index < len(s):
            times = 0
            char = s[index]
            while index < len(s) and s[index] == char:
                times += 1
                index += 1
            rs += str(times) + char
        return rs

# s = Solution()
# print(s.get_result("1211"))
# print(s.countAndSay(5))
